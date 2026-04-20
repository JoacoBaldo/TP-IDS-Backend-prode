def create_user_response(user: dict) -> dict:
    return {
        "email": user["email"],
        "name": user["name"],
        "message": "User created successfully",
        "status_code": 201
    }


def get_user_response(user: dict) -> dict:
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "status_code": 200
    }


def update_user_response(user: dict) -> dict:
    return {
        "email": user["email"],
        "name": user["name"],
        "message": "Usuario actualizado correctamente",
        "status_code": 200
    }


def get_users_list_response(users: list, total: int, page: int, limit: int) -> dict:
    return {
        "users": users,
        "message": "Users list retrieved successfully",
        "status_code": 200
    }