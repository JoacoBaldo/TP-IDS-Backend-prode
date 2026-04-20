from infrastructure.db_conn.mysql_config import get_connection

DEFAULT_PAGE = 1
DEFAULT_LIMIT = 10
DEFAULT_SORT_BY = 'created_at'
DEFAULT_ORDER = 'desc'


def get_users_list(page: int = DEFAULT_PAGE, limit: int = DEFAULT_LIMIT, sort_by: str = DEFAULT_SORT_BY, order: str = DEFAULT_ORDER):
    valid_fields = ['id', 'email', 'name', 'created_at']
    if sort_by not in valid_fields:
        sort_by = DEFAULT_SORT_BY
    
    conn = get_connection()
    try:
        with conn.cursor() as cursor:

            cursor.execute("SELECT COUNT(*) as total FROM users")
            total = cursor.fetchone()['total']
            
            offset = (page - 1) * limit
            cursor.execute(
                f"""
                SELECT id, email, name, created_at
                FROM users
                ORDER BY {sort_by} {order.upper()}
                LIMIT %s OFFSET %s
                """,
                (limit, offset)
            )
            users = cursor.fetchall()
            return users, total
    finally:
        conn.close()