from repository.users.get_users import get_users_list
from contracts.response.users_response import get_users_list_response


LIMIT = 10


def execute(page: int = 1, limit: int = LIMI):
   users, total = get_users_list(page, limit)
   return get_users_list_response(users, total, page, limit)

