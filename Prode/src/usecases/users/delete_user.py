from repository.users.delete_user_core import delete_user_core

def execute(user_id: int):
    user_deleted, err = delete_user_core(user_id)
    
    if err is not None:
        return {"status": "error", "message": err}
        
    return {"status": "success", "id_eliminado": user_deleted}