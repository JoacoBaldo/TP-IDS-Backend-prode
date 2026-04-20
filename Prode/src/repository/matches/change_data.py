from datetime import datetime, timezone

from infrastructure.db_conn.mysql_config import get_connection


_FIELD_MAP = {
    "equipo_local": "local_team",
    "equipo_visitante": "visitor_team",
    "fecha": "date_time",
    "fase": "phase",
    "estadio": "stadium",
    "ciudad": "city",
    "goles_local": "local_goals",
    "goles_visitante": "visitor_goals",
    "status": "status",
}


def _parse_fecha(fecha):
    if fecha is None:
        return None

    if not isinstance(fecha, str):
        raise ValueError("fecha debe ser una cadena ISO 8601")

    fecha = fecha.strip()
    if fecha == "":
        raise ValueError("fecha no puede estar vacía")

    if fecha.endswith("Z"):
        fecha = fecha[:-1] + "+00:00"

    fecha_dt = datetime.fromisoformat(fecha)
    if fecha_dt.tzinfo is not None:
        fecha_dt = fecha_dt.astimezone(timezone.utc).replace(tzinfo=None)

    return fecha_dt


def change_data(match_id: int, payload: dict):
    if not match_id:
        raise ValueError("Match ID is required")

    if not payload or not isinstance(payload, dict):
        return {"error": "No se proporcionaron campos para actualizar", "status_code": 400}

    updates = []
    values = []

    for field, value in payload.items():
        if field not in _FIELD_MAP:
            continue

        db_column = _FIELD_MAP[field]

        if field in {"equipo_local", "equipo_visitante", "fase", "estadio", "ciudad", "status"}:
            if value is not None and not isinstance(value, str):
                return {"error": f"{field} debe ser una cadena", "status_code": 400}
            if isinstance(value, str):
                value = value.strip()

        if field in {"goles_local", "goles_visitante"}:
            if not isinstance(value, int) or value < 0:
                return {"error": f"{field} debe ser un entero mayor o igual a cero", "status_code": 400}

        if field == "fecha":
            try:
                value = _parse_fecha(value)
            except ValueError as exc:
                return {"error": str(exc), "status_code": 400}

        updates.append(f"{db_column} = %s")
        values.append(value)

    if not updates:
        return {"error": "No se proporcionaron campos válidos para actualizar", "status_code": 400}

    query = f"UPDATE fixtures SET {', '.join(updates)} WHERE id = %s"
    values.append(match_id)

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, tuple(values))
            conn.commit()
            if cursor.rowcount == 0:
                return {"error": "Partido no encontrado", "status_code": 404}
    except Exception as exc:
        return {"error": str(exc), "status_code": 500}
    finally:
        conn.close()

    return None

    