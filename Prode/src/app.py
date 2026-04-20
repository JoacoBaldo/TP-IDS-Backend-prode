
import sys
import os
from infrastructure.entrypoints.users import users
from flask import Flask, Blueprint, request, jsonify
from usecases.users.update_user_use_case import execute as update_user_exec
from infrastructure.entrypoints.partidos import partidos
from infrastructure.entrypoints.ranking.ranking import get_ranking

app = Flask(__name__)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


users_bp = Blueprint('users', __name__, url_prefix='/users')
partidos_bp = Blueprint('partidos', __name__, url_prefix='/partidos')
ranking_bp = Blueprint('ranking', __name__, url_prefix='/ranking')


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

@partidos_bp.route('', methods=['GET'])
def get_partidos_endpoint():
    return partidos.get_partidos()


@partidos_bp.route('/<int:partido_id>', methods=['GET'])
def get_partido_by_id_endpoint(partido_id: int):
    return partidos.get_partido_by_id(partido_id)

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user_endpoint(user_id: int):
    return users.get_user(user_id)

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user_endpoint(user_id):
    return users.delete_usuario(user_id)
@app.route('/usuarios', methods=['GET'])
def get_users_list_endpoint():
    return users.get_users_list()


@partidos_bp.route('/<int:partido_id>/resultado', methods=['PUT'])
def put_resultado_endpoint(partido_id: int):
    return partidos.put_resultado(partido_id)

@partidos_bp.route('/<int:partido_id>', methods=['PUT'])
def put_replace_partido_endpoint(partido_id: int):
    return partidos.put_replace_partido(partido_id)

@partidos_bp.route('/<int:partido_id>', methods=['DELETE'])
def delete_partido_endpoint(partido_id: int):
    return partidos.delete_partido(partido_id)

@partidos_bp.route('/<int:partido_id>/prediccion', methods=['POST'])
def post_prediccion_endpoint(partido_id: int):
    return partidos.post_prediccion(partido_id)


@partidos_bp.route('', methods=['POST'])
def create_partido_endpoint():
    return partidos.post_partido()
@ranking_bp.route('/', methods=['GET'], strict_slashes=False)
def get_ranking_endpoint():
    return get_ranking()


app.register_blueprint(users_bp)
app.register_blueprint(partidos_bp)
app.register_blueprint(ranking_bp)



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
