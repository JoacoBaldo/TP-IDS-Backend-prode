from flask import request, jsonify
import usecases 
from contracts.request.users_request import create_user_request


def create_user():
    data = request.get_json()
    user_data = create_user_request(data)
    response = usecases.create_user.execute(user_data)
    
    return jsonify(response)