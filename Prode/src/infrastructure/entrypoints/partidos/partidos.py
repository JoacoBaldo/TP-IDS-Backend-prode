from flask import jsonify, request

from contracts.request.partidos_request import partido_reemplazo_request, partido_resultado_request, partido_creacion_request
from usecases.partidos.create_partido import execute as create_partido_execute
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


def post_partido():
    body = request.get_json() or {}
    payload = partido_creacion_request(body)
    return _as_http(create_partido_execute(payload))
