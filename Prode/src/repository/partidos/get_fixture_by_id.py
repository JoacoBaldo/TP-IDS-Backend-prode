from infrastructure.db_conn.mysql_config import get_connection


def get_fixture_by_id(fixture_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, local_team, visitor_team, stadium, city, date_time,
                       local_goals, visitor_goals, phase
                FROM fixtures
                WHERE id = %s
                """,
                (fixture_id,),
            )
            return cursor.fetchone()
    finally:
        conn.close()
