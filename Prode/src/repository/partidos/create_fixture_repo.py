from infrastructure.db_conn.mysql_config import get_connection
def create_fixture(partido_data):
    connection = None  
    try:
        connection = get_connection()
        cursor = connection.cursor()

        local_team = partido_data.get('equipo_local') 
        visitor_team = partido_data.get('equipo_visitante')
        date_time = partido_data.get('fecha')
        phase = partido_data.get('fase')

        sql = "INSERT INTO fixtures (local_team, visitor_team, date_time, phase) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (local_team, visitor_team, date_time, phase))
        
        nuevo_id = cursor.lastrowid 

        if nuevo_id:
            connection.commit()
            return {"id": nuevo_id}, None
        else:
            if connection:
                connection.rollback()
            return None, "No se pudo obtener el ID"

    except Exception as e:
        if connection:
            connection.rollback()
        print(f"Error en create_fixture: {e}")
        return None, str(e)

    finally:
        if connection:
            connection.close()


        