from infrastructure.db_conn.mysql_config import get_connection

DEFAULT_LIMIT = 20
MAX_LIMIT = 100


def count_users() -> int:
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS c FROM users")
            row = cursor.fetchone()
            return int(row["c"]) if row else 0
    finally:
        conn.close()


def fetch_ranking_page(limit: int, offset: int) -> list[dict]:
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT u.id AS id_usuario,
                       COALESCE(agg.puntos, 0) AS puntos
                FROM users u
                LEFT JOIN (
                    SELECT p.user_id,
                           SUM(
                               CASE
                                   WHEN p.predicted_local_goals = f.local_goals
                                        AND p.predicted_visitor_goals = f.visitor_goals
                                       THEN 3
                                   WHEN f.local_goals = f.visitor_goals
                                        AND p.predicted_local_goals = p.predicted_visitor_goals
                                       THEN 1
                                   WHEN (f.local_goals > f.visitor_goals
                                         AND p.predicted_local_goals > p.predicted_visitor_goals)
                                        OR (f.local_goals < f.visitor_goals
                                            AND p.predicted_local_goals < p.predicted_visitor_goals)
                                       THEN 1
                                   ELSE 0
                               END
                           ) AS puntos
                    FROM predictions p
                    INNER JOIN fixtures f ON p.fixture_id = f.id AND f.status = 'finished'
                    GROUP BY p.user_id
                ) agg ON u.id = agg.user_id
                ORDER BY puntos DESC, u.id ASC
                LIMIT %s OFFSET %s
                """,
                (limit, offset),
            )
            return cursor.fetchall()
    finally:
        conn.close()
