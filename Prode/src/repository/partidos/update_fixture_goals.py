from infrastructure.db_conn.mysql_config import get_connection


def update_fixture_goals(fixture_id: int, local_goals: int, visitor_goals: int) -> dict:
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE fixtures
                SET local_goals = %s, visitor_goals = %s
                WHERE id = %s
                """,
                (local_goals, visitor_goals, fixture_id),
            )
            conn.commit()
            if cursor.rowcount == 0:
                return {"error": "Partido no encontrado", "status_code": 404}
    except Exception as e:
        return {"error": str(e), "status_code": 500}
    finally:
        conn.close()
    return None
