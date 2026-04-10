from flask import request, jsonify
from usecases.users.create_user import execute
from contracts.request.users_request import create_user_request


def create_user():
    data = request.get_json()
    user_data = create_user_request(data)
    response = execute(user_data)
    
    return jsonify(response)