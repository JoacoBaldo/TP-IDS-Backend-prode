from flask import jsonify, request

from contracts.request.ranking_request import ranking_list_request
from usecases.ranking.get_ranking import execute as get_ranking_execute


def _as_http(resp: dict):
    code = resp.get("status_code", 200)
    body = resp.copy()
    body.pop("status_code", None)
    return jsonify(body), code


def get_ranking():
    params = ranking_list_request(request.args)
    resp = get_ranking_execute(**params)
    return _as_http(resp)
