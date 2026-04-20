from infrastructure.db_conn.mysql_config import get_connection


def get_users_ranking():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT u.name, COALESCE(r.total_points, 0) AS total_points
                FROM users u
                LEFT JOIN rankings r ON u.id = r.user_id
                ORDER BY total_points DESC, u.name ASC
                """,
            )
            rows = cursor.fetchall()
            return [f"{row['name']} {row['total_points']}" for row in rows]
    finally:
        conn.close()