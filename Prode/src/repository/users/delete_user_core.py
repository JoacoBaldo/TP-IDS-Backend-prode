from infrastructure.db_conn.mysql_config import get_connection

def delete_user_core(user_id: int):
    connection = None  
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query_predicciones = "DELETE FROM predicciones WHERE user_id = %s"
        cursor.execute(query_predicciones, (user_id,))

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