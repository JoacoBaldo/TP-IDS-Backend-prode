from flask import request, jsonify
from infrastructure.db_conn.mysql_config import get_connection
from contracts.request.users_request import create_user_request
from usecases.users.create_user import execute as create_user_execute


def create_user():
    data = request.get_json()
    user_data = create_user_request(data)
    response = create_user_execute(user_data)
    
    status_code = response.pop("status_code", 200)
    return jsonify(response), status_code


def get_user(user_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            if not user:
                return jsonify({"error": "Usuario no encontrado", "status_code": 404}), 404
            return jsonify({
                "id": user['id'],
                "name": user['name'],
                "email": user['email']
            }), 200
    finally:
        conn.close()