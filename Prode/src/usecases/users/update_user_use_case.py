import pymysql
from repository.users.update_users import update_user_repository
from infrastructure.errors.users import (
    ErrEmailAlreadyExists,
    ErrMissingInformation,
    ErrInvalidId,
    ErrUserNotFound,
    ErrEmptyBody
)
from contracts.response.users_response import update_user_response


def execute(user_id: int, user_req: dict) -> dict:
    if not user_req:
        return ErrEmptyBody

    try:
        user_id = int(user_id)
    except:
        return ErrInvalidId

    if not user_req.get("name") or not user_req.get("email"):
        return ErrMissingInformation

    try:
        updated = update_user_repository(user_id, user_req)

    except pymysql.err.IntegrityError:
        return ErrEmailAlreadyExists

    if updated:
        return update_user_response(user_req)

    return ErrUserNotFound