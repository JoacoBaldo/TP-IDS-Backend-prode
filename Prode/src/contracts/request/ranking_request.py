from repository.ranking.get_ranking import DEFAULT_LIMIT, MAX_LIMIT


def ranking_list_request(request_args) -> dict:
    return {
        "limit": request_args.get('limit', DEFAULT_LIMIT, type=int),
        "offset": request_args.get('offset', 0, type=int)
    }
