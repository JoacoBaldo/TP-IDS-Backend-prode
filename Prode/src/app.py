
import sys
import os
from infrastructure.entrypoints.users import users
from flask import Flask, Blueprint
from infrastructure.entrypoints.partidos import partidos

app = Flask(__name__)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


users_bp = Blueprint('users', __name__, url_prefix='/users')
partidos_bp = Blueprint('partidos', __name__, url_prefix='/partidos')


@users_bp.route('/register', methods=['POST'])
def create_user_endpoint():
    return users.create_user()


@partidos_bp.route('', methods=['GET'])
def get_partidos_endpoint():
    return partidos.get_partidos()


@partidos_bp.route('/<int:partido_id>', methods=['GET'])
def get_partido_by_id_endpoint(partido_id: int):
    return partidos.get_partido_by_id(partido_id)

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user_endpoint(user_id: int):
    return users.get_user(user_id)

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


app.register_blueprint(users_bp)
app.register_blueprint(partidos_bp)



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
