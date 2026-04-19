def _fecha_iso(value) -> str:
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


def partido_detalle_response(row: dict, status_code: int = 200) -> dict:
    return {
        "id": row["id"],
        "equipo_local": row["local_team"],
        "equipo_visitante": row["visitor_team"],
        "estadio": row.get("stadium"),
        "ciudad": row.get("city"),
        "fecha": _fecha_iso(row["date_time"]),
        "fase": row["phase"],
        "goles_local": row["local_goals"],
        "goles_visitante": row["visitor_goals"],
        "status_code": status_code,
    }


def prediccion_response(status_code: int = 201) -> dict:
    return {
        "status_code": status_code,
        "message": "Predicción registrada con éxito"
    }
