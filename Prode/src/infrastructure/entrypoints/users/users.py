from flask import request, jsonify
from contracts.request.users_request import create_user_request, get_users_list_request
from usecases.users.create_user import execute as create_user_execute
from usecases.users.get_users_list import execute as get_users_list_execute


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