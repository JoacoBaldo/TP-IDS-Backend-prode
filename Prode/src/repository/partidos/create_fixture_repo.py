from infrastructure.db_conn.mysql_config import get_connection
def create_fixture_repo(local_team, visitor_team, date_time, phase):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO fixtures (local_team, visitor_team, date_time, phase) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (local_team, visitor_team, date_time, phase))
            nuevo_id = cursor.lastrowid 
        conn.commit()
        return {"id": nuevo_id, "local_team": local_team, "visitor_team": visitor_team, "fecha": date_time, "fase": phase}, None
    except Exception as e:
        return None, {"error": str(e), "status_code": 500}
    finally:
        conn.close()