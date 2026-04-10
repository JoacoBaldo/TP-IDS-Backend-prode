from entities.users import User

def create_user_request(user: User) -> dict: 
    return {
        "email": user["email"],
        "name": user["name"],
        "password": user["password"]
    }