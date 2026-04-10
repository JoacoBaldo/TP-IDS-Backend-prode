
import sys
import os
from infrastructure.entrypoints.users import users
from flask import Flask, request
from contracts.request.users_request import create_user_request
from contracts.response.users_response import create_user_response
from config.swagger import init_swagger
from flasgger import swag_from

app = Flask(__name__)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
swagger = init_swagger(app)

@app.route('/register', methods=['POST'])
@swag_from('config/swagger_schemas/users_post.yml')
def create_user_endpoint():
    return users.create_user()





if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

