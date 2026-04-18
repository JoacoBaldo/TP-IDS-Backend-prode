from repository.users.update_users import update_user_repository, validate_email_exists


def execute(user_id: int, user_req: dict) -> dict:
    try:
        user_id = int(user_id)
    except:
        return {"error": "ID inválido", "status_code": 400}

    if not user_req.get("name") or not user_req.get("email"):
        return {"error": "Faltan datos", "status_code": 400}

    user_encontrado = validate_email_exists(user_req["email"], user_id)

    if user_encontrado:
        return {"error": "Email ya ocupado por otro", "status_code": 400}

    updated = update_user_repository(user_id, user_req)

    if updated:
        return {
            "message": "Usuario actualizado correctamente",
            "status_code": 200
        }

    return {
        "error": "No existe ese ID",
        "status_code": 404
    }