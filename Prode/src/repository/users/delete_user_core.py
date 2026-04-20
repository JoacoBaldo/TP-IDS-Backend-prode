from infrastructure.db_conn.mysql_config import get_connection

def delete_user_core(user_id: int):
    connection = None  
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # DB table is `predictions` (see schema.sql); it has ON DELETE CASCADE,
        # but we keep this delete for safety/legacy.
        query_predictions = "DELETE FROM predictions WHERE user_id = %s"
        cursor.execute(query_predictions, (user_id,))

        query_user = "DELETE FROM users WHERE id = %s"
        cursor.execute(query_user, (user_id,))

        connection.commit()
        return user_id, None

    except Exception as e:
        if connection:
            connection.rollback() 
        return None, str(e)

    finally:
        if connection:  
            connection.close()