from flask import jsonify, request

from contracts.request.partidos_request import partido_reemplazo_request, partido_resultado_request, prediccion_request
from usecases.partidos.replace_partido import execute as replace_partido_execute
from usecases.partidos.update_resultado import execute as update_resultado_execute
from usecases.partidos.create_prediction import execute as create_prediction_execute
from usecases.partidos.delete_partido import execute as delete_partido_execute


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


def delete_partido(partido_id: int):
    return _as_http(delete_partido_execute(partido_id))
  
def post_prediccion(partido_id: int):
    body = request.get_json() or {}
    prediction_data = prediccion_request(body)
    response = create_prediction_execute(partido_id, prediction_data)
    return _as_http(response)
