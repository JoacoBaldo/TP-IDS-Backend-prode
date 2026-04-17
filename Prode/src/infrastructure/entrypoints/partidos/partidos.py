from flask import Blueprint, jsonify, request

from contracts.request.partidos_request import partido_reemplazo_request, partido_resultado_request
from usecases.partidos.replace_partido import execute as replace_partido_execute
from usecases.partidos.update_resultado import execute as update_resultado_execute

partidos_bp = Blueprint("partidos", __name__, url_prefix="/partidos")


def _as_http(resp: dict):
    code = resp.get("status_code", 200)
    return jsonify(resp), code


@partidos_bp.route("/<int:partido_id>/resultado", methods=["PUT"])
def put_resultado(partido_id: int):
    body = request.get_json()
    payload = partido_resultado_request(body)
    return _as_http(update_resultado_execute(partido_id, payload))


@partidos_bp.route("/<int:partido_id>", methods=["PUT"])
def put_replace_partido(partido_id: int):
    body = request.get_json()
    payload = partido_reemplazo_request(body)
    return _as_http(replace_partido_execute(partido_id, payload))
