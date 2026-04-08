from entities import User

def create_user_request(user: User) -> dict: 
    return {
        "email": user["email"],
        "password": user["password"]
    }