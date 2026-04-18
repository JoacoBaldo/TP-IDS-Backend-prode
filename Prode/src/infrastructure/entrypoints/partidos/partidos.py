from flask import jsonify, request

from contracts.request.partidos_request import partido_reemplazo_request, partido_resultado_request
from usecases.partidos.replace_partido import execute as replace_partido_execute
from usecases.partidos.update_resultado import execute as update_resultado_execute
from usecases.partidos.get_partidos import execute as get_partidos_execute


def _as_http(resp: dict):
    code = resp.get("status_code", 200)
    return jsonify(resp), code


def get_partidos():
    equipo = request.args.get("equipo")
    fecha = request.args.get("fecha")
    fase = request.args.get("fase")
    try:
        limit = int(request.args.get("limit", 10))
        offset = int(request.args.get("offset", 0))
    except ValueError:
        return jsonify({"error": "limit y offset deben ser números enteros"}), 400
    respuesta = get_partidos_execute(equipo, fecha, fase, limit, offset)
    return _as_http(respuesta)


def put_resultado(partido_id: int):
    body = request.get_json() or {}
    payload = partido_resultado_request(body)
    return _as_http(update_resultado_execute(partido_id, payload))


def put_replace_partido(partido_id: int):
    body = request.get_json() or {}
    payload = partido_reemplazo_request(body)
    return _as_http(replace_partido_execute(partido_id, payload))
