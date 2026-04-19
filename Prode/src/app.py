
import sys
import os
from infrastructure.entrypoints.users import users
from infrastructure.entrypoints.partidos import partidos
from flask import Flask, Blueprint
from flask import request, jsonify
from usecases.users.update_user_use_case import execute as update_user_exec

app = Flask(__name__)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


users_bp = Blueprint('users', __name__, url_prefix='/users')
partidos_bp = Blueprint('partidos', __name__, url_prefix='/partidos')

@users_bp.route('/register', methods=['POST'])
def create_user_endpoint():
    return users.create_user()

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user_endpoint(user_id):
    user_req = request.get_json()

    if not user_req:
        return jsonify({"error": "Empty body"}), 400

    result = update_user_exec(user_id, user_req)

    return jsonify(result), result.get("status_code", 200)

@partidos_bp.route('/<int:partido_id>/resultado', methods=['PUT'])
def put_resultado_endpoint(partido_id: int):
    return partidos.put_resultado(partido_id)


@partidos_bp.route('/<int:partido_id>', methods=['PUT'])
def put_replace_partido_endpoint(partido_id: int):
    return partidos.put_replace_partido(partido_id)


app.register_blueprint(users_bp)
app.register_blueprint(partidos_bp)



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

