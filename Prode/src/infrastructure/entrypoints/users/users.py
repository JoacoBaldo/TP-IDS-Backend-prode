from flask import request, jsonify
from contracts.request.users_request import create_user_request
from usecases.users.create_user import execute as create_user_execute


def create_user():
    data = request.get_json()
    user_data = create_user_request(data)
    response = create_user_execute(user_data)
    
    return jsonify(response)