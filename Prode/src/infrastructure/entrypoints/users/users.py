from flask import request, jsonify
from contracts.request.users_request import create_user_request
from usecases.users.create_user import execute as create_user_execute
from usecases.users.get_users_ranking import execute as get_users_ranking_execute
from usecases.users.get_users_list import execute as get_users_list_execute


def create_user():
    data = request.get_json()
    user_data = create_user_request(data)
    response = create_user_execute(user_data)

    status_code = response.pop("status_code", 200)
    return jsonify(response), status_code


def get_users_ranking():
    response = get_users_ranking_execute()

    status_code = response.pop("status_code", 200)
    return jsonify(response), status_code


def get_users_list():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    if page < 1:
        page = 1
    if limit < 1 or limit > 100:
        limit = 10
    
    response = get_users_list_execute(page, limit)

    status_code = response.pop("status_code", 200)
    return jsonify(response), status_code