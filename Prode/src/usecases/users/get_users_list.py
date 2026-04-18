from repository.users.get_users import get_users_list
from contracts.response.users_response import get_users_list_response


def execute(page: int = 1, limit: int = 10):
    users, total = get_users_list(page, limit)
    return get_users_list_response(users, total, page, limit)