from infrastructure.errors.users import ErrEmailAlreadyExists, ErrMissingEmailOrPassword, ErrPasswordTooShort, ErrInvalidEmailFormat
from Prode.src.contracts.response.users_response import create_user_response
from repository.users.create_users import create_UserRepository
from entities import User

def execute(user_req: User) -> dict:

    if validate_user_data(user_req) != None:
        return validate_user_data(user_req)
    
    if validate_email_exists(user_req["email"]):
        return ErrEmailAlreadyExists

    err = create_UserRepository(user_req)
    if err != None:
        return err

    return create_user_response(user_req)


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