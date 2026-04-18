from infrastructure.db_conn.mysql_config import get_connection
import pymysql


def update_user_repository(user_id, user_data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        user_id = int(user_id)

        query = "UPDATE prode.users SET name = %s, email = %s WHERE id = %s"
        cursor.execute(query, (user_data['name'], user_data['email'], user_id))
        conn.commit()

        if cursor.rowcount > 0:
            return True

        cursor.execute("SELECT id FROM prode.users WHERE id = %s", (user_id,))
        exists = cursor.fetchone()

        return exists is not None

    finally:
        cursor.close()
        conn.close()

def validate_email_exists(email, user_id):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        query = "SELECT id FROM prode.users WHERE email = %s AND id != %s"
        cursor.execute(query, (email, user_id))
        user = cursor.fetchone()
        return user

    finally:
        cursor.close()
        conn.close()