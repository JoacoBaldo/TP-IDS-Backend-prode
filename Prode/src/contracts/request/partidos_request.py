def partido_resultado_request(data) -> dict:
    if not data:
        return {}
    return {
        "goles_local": data.get("goles_local"),
        "goles_visitante": data.get("goles_visitante"),
    }


def partido_reemplazo_request(data) -> dict:
    if not data:
        return {}
    return {
        "equipo_local": data.get("equipo_local"),
        "equipo_visitante": data.get("equipo_visitante"),
        "fecha": data.get("fecha"),
        "fase": data.get("fase"),
    }
