from infrastructure.db_conn.mysql_config import get_connection


def get_UserRepository(user_id: int) -> dict:
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            return user
    finally:
        conn.close()
