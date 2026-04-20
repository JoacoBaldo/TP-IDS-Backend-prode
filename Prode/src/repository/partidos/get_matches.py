from infrastructure.db_conn.mysql_config import get_connection

def get_partidos_repo(equipo: str, fecha: str, fase: str, limit: int, offset: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            query_filtros = ""
            valores = []
            if equipo:
                query_filtros += " AND (local_team LIKE %s OR visitor_team LIKE %s)"
                valores.extend([f"%{equipo}%", f"%{equipo}%"])
            if fecha:
                query_filtros += " AND DATE(date_time) = %s"
                valores.append(fecha)
            if fase:
                query_filtros += " AND phase = %s"
                valores.append(fase)

            query_total = f"SELECT COUNT(*) AS total FROM fixtures WHERE 1=1 {query_filtros}"
            cursor.execute(query_total, tuple(valores))
            total = int(cursor.fetchone()["total"])

            query_datos = f"""
                SELECT id, local_team, visitor_team, date_time, phase 
                FROM fixtures 
                WHERE 1=1 {query_filtros} 
                LIMIT %s OFFSET %s
            """
            valores_finales = valores + [limit, offset]
            cursor.execute(query_datos, tuple(valores_finales))
            rows = cursor.fetchall()

            items = []
            for row in rows:
                items.append({
                    "id": row["id"],
                    "equipo_local": row["local_team"],
                    "equipo_visitante": row["visitor_team"],
                    "fecha": str(row["date_time"]),
                    "fase": row["phase"],
                })

            return items, total

    except Exception as e:
        return None, 0
    finally:
        conn.close()