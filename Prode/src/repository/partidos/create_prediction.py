from infrastructure.db_conn.mysql_config import get_connection
from entities.predictions import Prediction


def create_PredictionRepository(partido_id: int, prediction: Prediction) -> dict:
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO predictions (user_id, fixture_id, predicted_local_goals, predicted_visitor_goals) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (prediction['user_id'], partido_id, prediction['predicted_local_goals'], prediction['predicted_visitor_goals']))
            conn.commit()
    except Exception as e:
        return {"error": str(e), "status_code": 500}
    finally:
        conn.close()
    return None
