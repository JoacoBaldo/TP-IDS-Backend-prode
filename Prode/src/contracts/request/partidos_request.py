def partido_resultado_request(data) -> dict:
    return {
        "goles_local": data.get("goles_local"),
        "goles_visitante": data.get("goles_visitante"),
    }


def partido_reemplazo_request(data) -> dict:
    return {
        "equipo_local": data.get("equipo_local"),
        "equipo_visitante": data.get("equipo_visitante"),
        "fecha": data.get("fecha"),
        "fase": data.get("fase"),
    }


def prediccion_request(data) -> dict:
    return {
        "user_id": data.get("id_usuario"),
        "predicted_local_goals": data.get("local"),
        "predicted_visitor_goals": data.get("visitante"),
    }
