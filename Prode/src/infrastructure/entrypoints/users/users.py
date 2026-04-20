from usecases.users.delete_user import execute as delete_user_execute
from flask import request, jsonify
from contracts.request.users_request import create_user_request, get_users_list_request
from usecases.users.create_user import execute as create_user_execute
from usecases.users.get_users_list import execute as get_users_list_execute
from usecases.users.get_user import execute as get_user_execute
from usecases.users.update_user_use_case import execute as update_user_execute


def create_user():
    data = request.get_json()
    user_data = create_user_request(data)
    response = create_user_execute(user_data)
    status_code = response.pop("status_code", 200)
    return jsonify(response), status_code


def get_users_list():
    list_params = get_users_list_request(request.args)
    response = get_users_list_execute(**list_params)
    status_code = response.pop("status_code", 200)
    return jsonify(response), status_code


def get_user(user_id: int):
    response = get_user_execute(user_id)
    status_code = response.pop("status_code", 200)
    return jsonify(response), status_code


def update_user(user_id: int):
    user_req = request.get_json()
    response = update_user_execute(user_id, user_req)

    status_code = response.pop("status_code", 200)
    return jsonify(response), status_code
def delete_usuario(user_id: int):
    response = delete_user_execute(user_id)
    status_code = response.pop("status_code", 200)
    return jsonify(response), status_code
