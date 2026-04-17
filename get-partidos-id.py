from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'prode_user',
    'password': 'prode_pass123',
    'database': 'prode',
    'port': 3306
}

def construir_filtros_sql(equipo, fecha, fase):
    
    query_filtros = ""
    valores = []

    if equipo:
        query_filtros += " AND (equipo_local LIKE %s OR equipo_visitante LIKE %s)"
        valores.extend([f"%{equipo}%", f"%{equipo}%"])
    
    if fecha:
        query_filtros += " AND fecha = %s"
        valores.append(fecha)
    
    if fase:
        query_filtros += " AND fase = %s"
        valores.append(fase)

    return query_filtros, valores

def generar_links_paginacion(total, limit, offset, base_url="/partidos"):
    """
    Calcula las páginas y genera los enlaces obligatorios: first, prev, next, last.
    """
    if total == 0:
        last_offset = 0
    else:
        last_offset = ((total - 1) // limit) * limit

    _links = {
        "first": f"{base_url}?limit={limit}&offset=0",
        "last": f"{base_url}?limit={limit}&offset={last_offset}"
    }

    if offset > 0:
        prev_offset = max(0, offset - limit)
        _links["prev"] = f"{base_url}?limit={limit}&offset={prev_offset}"

    if (offset + limit) < total:
        next_offset = offset + limit
        _links["next"] = f"{base_url}?limit={limit}&offset={next_offset}"

    return _links

@app.route("/partidos", methods=["GET"])
def listar_partidos():
    #parámetros para el PDF
    equipo = request.args.get("equipo")
    fecha = request.args.get("fecha")
    fase = request.args.get("fase")

    try:
        limit = int(request.args.get("limit", 10))
        offset = int(request.args.get("offset", 0))
        if limit < 1 or offset < 0:
            return jsonify({"error": "limit debe ser > 0 y offset >= 0"}), 400
    except ValueError:
        return jsonify({"error": "limit y offset deben ser números enteros"}), 400

    #conecta con la db
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        puntero = conexion.cursor(dictionary=True)
        
        #filtramos con la otra función
        condiciones_sql, valores_filtros = construir_filtros_sql(equipo, fecha, fase)

        #total de partidos
        query_total = f"SELECT COUNT(*) AS total FROM partidos WHERE 1=1 {condiciones_sql}"
        puntero.execute(query_total, tuple(valores_filtros))
        total_registros = puntero.fetchone()["total"]

        query_datos = f"""
            SELECT id, equipo_local, equipo_visitante, fecha, fase 
            FROM partidos 
            WHERE 1=1 {condiciones_sql} 
            LIMIT %s OFFSET %s
        """
        valores_finales = valores_filtros + [limit, offset]
        puntero.execute(query_datos, tuple(valores_finales))
        datos_partidos = puntero.fetchall()

        for p in datos_partidos:
            if 'fecha' in p and p['fecha']:
                p['fecha'] = str(p['fecha'])

        #armo links con los filtros
        links = generar_links_paginacion(total_registros, limit, offset)

        return jsonify({
            "items": datos_partidos,
            "total": total_registros,
            "_links": links
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'puntero' in locals(): puntero.close()
        if 'conexion' in locals(): conexion.close()

if __name__ == "__main__":
    app.run(debug=True)