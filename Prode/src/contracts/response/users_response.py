def create_user_response(user: dict) -> dict:
    return {
        "email": user["email"],
        "name": user["name"],
        "message": "User created successfully",
        "status_code": 201
    }


def get_users_ranking_response(users: list) -> dict:
    return {
        "users": users,
        "message": "Users ranking retrieved successfully",
        "status_code": 200
    }


def get_users_list_response(users: list, total: int, page: int, limit: int) -> dict:
    return {
        "users": users,
        "pagination": {
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": (total + limit - 1) // limit  
        },
        "message": "Users list retrieved successfully",
        "status_code": 200
    }