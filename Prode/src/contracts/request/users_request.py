from entities.users import User
from repository.users.get_users import DEFAULT_PAGE, DEFAULT_LIMIT, DEFAULT_SORT_BY, DEFAULT_ORDER

def create_user_request(user: User) -> dict: 
    return {
        "email": user.get("email"),
        "name": user.get("name"),
        "password": user.get("password")
    }


def get_users_list_request(request_args) -> dict:
    return {
        "page": request_args.get('page', DEFAULT_PAGE, type=int),
        "limit": request_args.get('limit', DEFAULT_LIMIT, type=int),
        "sort_by": request_args.get('sort_by', DEFAULT_SORT_BY, type=str),
        "order": request_args.get('order', DEFAULT_ORDER, type=str)
    }