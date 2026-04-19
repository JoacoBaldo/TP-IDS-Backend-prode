from repository.users.ranking import get_users_ranking
from contracts.response.users_response import get_users_ranking_response


def execute():
    users = get_users_ranking()
    return get_users_ranking_response(users)