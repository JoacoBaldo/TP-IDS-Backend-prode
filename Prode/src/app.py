
from Prode.src.infrastructure.entrypoints.users import users
from flask import Flask, request
from contracts.request.users_request import create_user_request
from Prode.src.contracts.response.users_response import create_user_response

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user_endpoint():
    return users.create_user()

