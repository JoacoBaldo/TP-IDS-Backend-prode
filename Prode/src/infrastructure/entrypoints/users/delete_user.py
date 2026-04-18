from src.repository.users.delete_user_core import delete_user_core

def execute(user_id: int) -> dict:
    # Esta es la función que limpia todas las tablas de la DB
    success, err = delete_user_core(user_id)
    if err is not None:
        return err
    return {"message": f"Usuario {user_id} eliminado", "status_code": 200}