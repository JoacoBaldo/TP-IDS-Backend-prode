from infrastructure.db_conn.mysql_config import get_connection
from infrastructure.errors.users import ErrEmailAlreadyExists
from entities.users import User
import pymysql

def create_UserRepository(user: User) -> dict:
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (email, name, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user['email'], user['name'], user['password']))
            conn.commit()
    
    except pymysql.err.IntegrityError as e:
        if e.args[0] == 1062:
            return ErrEmailAlreadyExists
        return {"error": str(e), "status_code": 500}
    
    except Exception as e:
        return {"error": str(e), "status_code": 500}
    
    finally:
        conn.close()
    return None
