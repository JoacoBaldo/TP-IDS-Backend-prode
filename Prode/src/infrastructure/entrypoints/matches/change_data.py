from datetime import datetime
from infrastructure.db_conn.mysql_config import get_connection
from infrastructure.errors.partidos import *

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
    try:
        if not isinstance(fecha, str) or not fecha.strip():
            return ErrFechaInvalida
        return datetime.fromisoformat(fecha.replace("Z", "+00:00"))
    except:
        return ErrFechaInvalida

def change_data(match_id: int, payload: dict):
    try:
        if not match_id:
            return ErrPartidoIdInvalido

        if not payload or not isinstance(payload, dict):
            return ErrNoCamposParaActualizar

        updates, values = [], []

        for field, value in payload.items():
            if field not in _FIELD_MAP:
                continue

            if field in {"goles_local", "goles_visitante"}:
                if not isinstance(value, int) or value < 0:
                    return ErrGolesInvalidos

            if field in {"equipo_local", "equipo_visitante"}:
                if not isinstance(value, str) or not value.strip():
                    return ErrEquipoVacio
                value = value.strip()

            if field == "fase":
                if not isinstance(value, str) or not value.strip():
                    return ErrFaseVacia
                value = value.strip()

            if field == "fecha":
                parsed = _parse_fecha(value)
                if isinstance(parsed, dict):
                    return parsed
                value = parsed

            if field in {"estadio", "ciudad", "status"}:
                if value is not None and not isinstance(value, str):
                    return ErrCamposInvalidos
                if isinstance(value, str):
                    value = value.strip()

            updates.append(f"{_FIELD_MAP[field]} = %s")
            values.append(value)

        if not updates:
            return ErrCamposInvalidos

        query = f"UPDATE fixtures SET {', '.join(updates)} WHERE id = %s"
        values.append(match_id)

        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, tuple(values))
                conn.commit()   
                if cursor.rowcount == 0:
                    return ErrPartidoNotFound
        finally:
            conn.close()

        return None

    except Exception:
        return {"error": "Error interno", "status_code": 500}