
import sys
import os
from infrastructure.entrypoints.users import users
from flask import Flask, request, Blueprint
from contracts.request.users_request import create_user_request
from contracts.response.users_response import create_user_response

app = Flask(__name__)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/register', methods=['POST'])
def create_user_endpoint():
    return users.create_user()

app.register_blueprint(users_bp)





if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

