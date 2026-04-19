
import sys
import os
from infrastructure.entrypoints.users import users
from infrastructure.entrypoints.matches.delete_match import delete_match
from flask import Flask, request, Blueprint
from contracts.request.users_request import create_user_request
from contracts.response.users_response import create_user_response
from infrastructure.entrypoints.partidos import partidos

app = Flask(__name__)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


users_bp = Blueprint('users', __name__, url_prefix='/users')
partidos_bp = Blueprint('partidos', __name__, url_prefix='/partidos')
matches_bp = Blueprint('matches', __name__, url_prefix='/matches')

@users_bp.route('/register', methods=['POST'])
def create_user_endpoint():
    return users.create_user()

@matches_bp.route('/<int:match_id>', methods=['DELETE'])
def delete_match_endpoint(match_id):
    return delete_match(match_id)

@partidos_bp.route('/<int:partido_id>/resultado', methods=['PUT'])
def put_resultado_endpoint(partido_id: int):
    return partidos.put_resultado(partido_id)

@partidos_bp.route('/<int:partido_id>', methods=['PUT'])
def put_replace_partido_endpoint(partido_id: int):
    return partidos.put_replace_partido(partido_id)

app.register_blueprint(matches_bp)
app.register_blueprint(users_bp)
app.register_blueprint(partidos_bp)



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

