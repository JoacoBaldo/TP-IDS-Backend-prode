from infrastructure.db_conn.mysql_config import get_connection

def delete_match(match_id):
    if not match_id:
        raise ValueError("Match ID is required")
    
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        # Ejecutar el delete
        query = "DELETE FROM fixtures WHERE id = %s"
        cursor.execute(query, (match_id,))
        connection.commit()
        
        if cursor.rowcount > 0:
            return {"message": "Match deleted successfully", "status_code": 200}
        else:
            return {"message": "Match not found", "status_code": 404}
    except Exception as e:
        return {"error": str(e), "status_code": 500}
    finally:
        cursor.close()
        connection.close()