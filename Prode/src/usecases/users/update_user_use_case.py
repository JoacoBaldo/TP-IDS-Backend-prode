import pymysql
from repository.users.update_users import update_user_repository
from infrastructure.errors.users import (
    ErrEmailAlreadyExists,
    ErrMissingInformation,
    ErrInvalidId
)


def execute(user_id: int, user_req: dict) -> dict:
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
        return {
            "message": "Usuario actualizado correctamente",
            "status_code": 200
        }

    return {
        "error": "User not found",
        "status_code": 404
    }