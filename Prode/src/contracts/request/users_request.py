from entities.users import User

def create_user_request(user: User) -> dict: 
    return {
        "email": user.get("email"),
        "name": user.get("name"),
        "password": user.get("password")
    }