def create_user_response(user: dict) -> dict:
    return {
        "email": user["email"],
        "message": "User created successfully",
        "status_code": 201
    }