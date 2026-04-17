from infrastructure.db_conn.mysql_config import get_connection


def replace_fixture_core(
    fixture_id: int,
    local_team: str,
    visitor_team: str,
    date_time,
    phase: str,
) -> dict:
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE fixtures
                SET local_team = %s, visitor_team = %s, date_time = %s, phase = %s
                WHERE id = %s
                """,
                (local_team, visitor_team, date_time, phase, fixture_id),
            )
            conn.commit()
            if cursor.rowcount == 0:
                return {"error": "Partido no encontrado", "status_code": 404}
    except Exception as e:
        return {"error": str(e), "status_code": 500}
    finally:
        conn.close()
    return None
