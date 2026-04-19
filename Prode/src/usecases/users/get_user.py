from infrastructure.errors.users import ErrUserNotFound
from contracts.response.users_response import get_user_response
from repository.users.get_user import get_UserRepository


def execute(user_id: int) -> dict:
    user = get_UserRepository(user_id)
    if not user:
        return ErrUserNotFound
    return get_user_response(user)
