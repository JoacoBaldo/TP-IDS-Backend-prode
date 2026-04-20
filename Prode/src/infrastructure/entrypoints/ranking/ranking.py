from flask import jsonify, request

from contracts.request.ranking_request import ranking_list_params
from infrastructure.errors.ranking import ErrRankingPaginacionInvalida
from usecases.ranking.get_ranking import execute as get_ranking_execute


def _as_http(resp: dict):
    code = resp.get("status_code", 200)
    body = resp.copy()
    body.pop("status_code", None)
    return jsonify(body), code


def get_ranking():
    params = ranking_list_params(request.args)
    if not params.get("ok"):
        return _as_http(ErrRankingPaginacionInvalida)

    resp = get_ranking_execute(
        params["limit"],
        params["offset"],
        request.base_url,
        params["max_limit"],
    )
    return _as_http(resp)
