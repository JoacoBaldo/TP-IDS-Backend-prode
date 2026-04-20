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