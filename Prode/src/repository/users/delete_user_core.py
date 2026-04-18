from infrastructure.db_conn.db_connection import get_db_connection

def delete_user_core(user_id: int):

    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
        return user_id, None
        
    except Exception as e:
        return None, str(e)
    
    finally:
        cursor.close()
        connection.close()