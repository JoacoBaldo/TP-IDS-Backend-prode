def create_user_response(user: dict) -> dict:
    return {
        "email": user["email"],
        "name": user["name"],
        "message": "User created successfully",
        "status_code": 201
    }