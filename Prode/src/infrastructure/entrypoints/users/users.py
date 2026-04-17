from flask import request, jsonify
from usecases.users import create_user as create_user_usecase
from contracts.request.users_request import create_user_request


def create_user():
    data = request.get_json()
    user_data = create_user_request(data)
    response = create_user_usecase.execute(user_data)
    
    status_code = response.pop("status_code", 200)
    return jsonify(response), status_code