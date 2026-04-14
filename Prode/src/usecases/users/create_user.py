from infrastructure.errors.users import ErrEmailAlreadyExists, ErrMissingEmailOrPassword, ErrPasswordTooShort, ErrInvalidEmailFormat
from contracts.response.users_response import create_user_response
from repository.users.create_users import create_UserRepository
from entities.users import User
import bcrypt

def execute(user_req: User) -> dict:

    if validate_user_data(user_req) != None:
        return validate_user_data(user_req)
    
    if validate_email_exists(user_req["email"]):
        return ErrEmailAlreadyExists

    hashed_password = hash_password(user_req["password"])
    user_req["password"] = hashed_password

    err = create_UserRepository(user_req)
    if err != None:
        return err

    user_response = user_req.copy()
    del user_response["password"]
    return create_user_response(user_response)


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def validate_user_data(user_req: User) -> dict:
    if not user_req.get("email") or not user_req.get("password"):
        return ErrMissingEmailOrPassword

    if len(user_req["password"]) < 6:
        return ErrPasswordTooShort
    
    if "@" not in user_req["email"]:
        return ErrInvalidEmailFormat

    return None


def validate_email_exists(email: str) -> bool:
    # Aquí iría la lógica para verificar si el email ya existe en la base de datos
    return False