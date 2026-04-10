from infrastructure.db_conn.mysql_config import get_connection
from entities.users import User

def create_UserRepository(user: User) -> dict:
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (email, name, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user['email'], user['name'], user['password']))
            conn.commit()
    
    except Exception as e:
        return {"error": str(e), "status_code": 500}
    
    finally:
        conn.close()
    return None
