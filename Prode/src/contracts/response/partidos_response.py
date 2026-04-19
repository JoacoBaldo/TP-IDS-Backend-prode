def _fecha_iso(value) -> str:
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


def partido_detalle_response(row: dict, status_code: int = 201) -> dict:
    return {
        "id": row.get("id"),
        "equipo_local": row.get("local_team"),
        "equipo_visitante": row.get("visitor_team"),
        "estadio": row.get("stadium"),
        "ciudad": row.get("city"),
        "fecha": _fecha_iso(row.get("date_time")) if row.get("date_time") else None,
        "fase": row.get("phase"), 
        "goles_local": row.get("local_goals"),
        "goles_visitante": row.get("visitor_goals"),
        "status_code": status_code,
    }
