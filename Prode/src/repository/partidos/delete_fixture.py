from infrastructure.db_conn.mysql_config import get_connection


def delete_fixture(fixture_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM fixtures WHERE id = %s", (fixture_id,))
            conn.commit()
            if cursor.rowcount == 0:
                return {"error": "Partido no encontrado", "status_code": 404}
    except Exception as e:
        return {"error": str(e), "status_code": 500}
    finally:
        conn.close()
    return None
