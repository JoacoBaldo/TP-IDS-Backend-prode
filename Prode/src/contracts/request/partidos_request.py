def partido_resultado_request(data) -> dict:
    return {
        "local_goals": data.get("goles_local"),
        "visitor_goals": data.get("goles_visitante"),
    }


def partido_reemplazo_request(data) -> dict:
    return {
        "local_team": data.get("equipo_local"),
        "visitor_team": data.get("equipo_visitante"),
        "date_time": data.get("fecha"),
        "phase": data.get("fase"),
    }


def partido_creacion_request(body):
    return {
        "local_team": body.get("equipo_local"),
        "visitor_team": body.get("equipo_visitante"),
        "date_time": body.get("fecha"),
        "phase": body.get("fase"),
    }


def prediccion_request(data) -> dict:
    return {
        "user_id": data.get("id_usuario"),
        "predicted_local_goals": data.get("local"),
        "predicted_visitor_goals": data.get("visitante"),
    }
