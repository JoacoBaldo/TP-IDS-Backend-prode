from repository.ranking.ranking import get_users_ranking
from contracts.response.users_response import get_users_ranking_response


def execute() -> dict:
    rankings = get_users_ranking()
    return get_users_ranking_response(rankings)
