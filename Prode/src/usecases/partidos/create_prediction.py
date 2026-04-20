from datetime import datetime
from infrastructure.errors.partidos import (
    ErrMissingFields,
    ErrInvalidFieldType,
    ErrInvalidGoals,
    ErrUserNotFound,
    ErrPartidoNotFound,
    ErrPartidoAlreadyPlayed,
    ErrPredictionAlreadyExists
)
from contracts.response.partidos_response import prediccion_response
from repository.partidos.create_prediction import create_PredictionRepository
from entities.predictions import Prediction


def execute(partido_id: int, prediction_req: Prediction) -> dict:
    if validate_prediction_data(prediction_req) != None:
        return validate_prediction_data(prediction_req)
    
    if validate_user_exists(prediction_req["user_id"]):
        return ErrUserNotFound
    
    if validate_partido_exists(partido_id):
        return ErrPartidoNotFound
    
    if validate_partido_not_played(partido_id):
        return ErrPartidoAlreadyPlayed
    
    if validate_prediction_not_exists(prediction_req["user_id"], partido_id):
        return ErrPredictionAlreadyExists
    
    err = create_PredictionRepository(partido_id, prediction_req)
    if err != None:
        return err
    
    return prediccion_response()


def validate_prediction_data(prediction: Prediction) -> dict:
    if prediction.get("user_id") is None or prediction.get("predicted_local_goals") is None or prediction.get("predicted_visitor_goals") is None:
        return ErrMissingFields
    
    if type(prediction["user_id"]) is not int or type(prediction["predicted_local_goals"]) is not int or type(prediction["predicted_visitor_goals"]) is not int:
        return ErrInvalidFieldType
    
    if prediction["predicted_local_goals"] < 0 or prediction["predicted_visitor_goals"] < 0:
        return ErrInvalidGoals
    
    return None


def validate_user_exists(user_id: int) -> bool:
    from infrastructure.db_conn.mysql_config import get_connection
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
            return not cursor.fetchone()
    finally:
        conn.close()


def validate_partido_exists(partido_id: int) -> bool:
    from infrastructure.db_conn.mysql_config import get_connection
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT date_time FROM fixtures WHERE id = %s", (partido_id,))
            return not cursor.fetchone()
    finally:
        conn.close()


def validate_partido_not_played(partido_id: int) -> bool:
    from infrastructure.db_conn.mysql_config import get_connection
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT date_time FROM fixtures WHERE id = %s", (partido_id,))
            partido = cursor.fetchone()
            if partido and partido['date_time'] and partido['date_time'] < datetime.now():
                return True
            return False
    finally:
        conn.close()


def validate_prediction_not_exists(user_id: int, partido_id: int) -> bool:
    from infrastructure.db_conn.mysql_config import get_connection
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM predictions WHERE user_id = %s AND fixture_id = %s", (user_id, partido_id))
            return bool(cursor.fetchone())
    finally:
        conn.close()
