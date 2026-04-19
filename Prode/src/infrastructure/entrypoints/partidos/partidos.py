from flask import jsonify, request
from datetime import datetime
from infrastructure.db_conn.mysql_config import get_connection

from contracts.request.partidos_request import partido_reemplazo_request, partido_resultado_request
from usecases.partidos.replace_partido import execute as replace_partido_execute
from usecases.partidos.update_resultado import execute as update_resultado_execute

def _as_http(resp: dict):
    code = resp.get("status_code", 200)
    return jsonify(resp), code


def put_resultado(partido_id: int):
    body = request.get_json() or {}
    payload = partido_resultado_request(body)
    return _as_http(update_resultado_execute(partido_id, payload))


def put_replace_partido(partido_id: int):
    body = request.get_json() or {}
    payload = partido_reemplazo_request(body)
    return _as_http(replace_partido_execute(partido_id, payload))


def post_prediccion(partido_id: int):
    body = request.get_json() or {}
    id_usuario = body.get("id_usuario")
    local = body.get("local")
    visitante = body.get("visitante")

    if id_usuario is None or local is None or visitante is None:
        return jsonify({"error": "id_usuario, local y visitante son obligatorios", "status_code": 400}), 400

    if type(local) is not int or type(visitante) is not int or type(id_usuario) is not int:
        return jsonify({"error": "id_usuario, local y visitante son obligatorios", "status_code": 400}), 400

    if local < 0 or visitante < 0:
        return jsonify({"error": "id_usuario, local y visitante son obligatorios", "status_code": 400}), 400

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM users WHERE id = %s", (id_usuario,))
            if not cursor.fetchone():
                return jsonify({"error": "Usuario no encontrado", "status_code": 404}), 404

            cursor.execute("SELECT date_time FROM fixtures WHERE id = %s", (partido_id,))
            partido = cursor.fetchone()
            if not partido:
                return jsonify({"error": "Partido no encontrado", "status_code": 404}), 404
            
            if partido['date_time'] and partido['date_time'] < datetime.now():
                return jsonify({"error": "El partido ya se ha jugado", "status_code": 400}), 400

            cursor.execute("SELECT id FROM predictions WHERE user_id = %s AND fixture_id = %s", (id_usuario, partido_id))
            if cursor.fetchone():
                return jsonify({"error": "El usuario ya tiene una predicción para este partido", "status_code": 409}), 409

            cursor.execute(
                "INSERT INTO predictions (user_id, fixture_id, predicted_local_goals, predicted_visitor_goals) VALUES (%s, %s, %s, %s)",
                (id_usuario, partido_id, local, visitante)
            )
            conn.commit()
            return jsonify({"status_code": 201, "message": "Predicción registrada con éxito"}), 201
    finally:
        conn.close()
