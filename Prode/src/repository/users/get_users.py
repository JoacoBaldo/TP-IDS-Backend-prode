from infrastructure.db_conn.mysql_config import get_connection


def get_users_list(page: int = 1, limit: int = 10):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:

            cursor.execute("SELECT COUNT(*) as total FROM users")
            total = cursor.fetchone()['total']
            
            offset = (page - 1) * limit
            cursor.execute(
                """
                SELECT id, email, name, created_at
                FROM users
                ORDER BY created_at DESC
                LIMIT %s OFFSET %s
                """,
                (limit, offset)
            )
            users = cursor.fetchall()
            return users, total
    finally:
        conn.close()