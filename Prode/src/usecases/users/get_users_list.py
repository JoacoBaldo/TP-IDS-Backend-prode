from repository.users.get_users import get_users_list, DEFAULT_PAGE, DEFAULT_LIMIT, DEFAULT_SORT_BY, DEFAULT_ORDER
from contracts.response.users_response import get_users_list_response


def execute(page: int = DEFAULT_PAGE, limit: int = DEFAULT_LIMIT, sort_by: str = DEFAULT_SORT_BY, order: str = DEFAULT_ORDER):
    
    if page < 1:
        page = DEFAULT_PAGE
    if limit < 1 or limit > 100:
        limit = DEFAULT_LIMIT
    if order.lower() not in ['asc', 'desc']:
        order = DEFAULT_ORDER
    else:
        order = order.lower()
    
    users, total = get_users_list(page, limit, sort_by, order)
    return get_users_list_response(users, total, page, limit)