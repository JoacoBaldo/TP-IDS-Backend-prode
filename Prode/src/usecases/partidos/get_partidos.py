from repository.partidos.get_matches import get_partidos_repo

def execute(equipo: str, fecha: str, fase: str, limit: int, offset: int) -> dict:
    if limit < 1:
        limit = 10
    if offset < 0:
        offset = 0

    items, total = get_partidos_repo(equipo, fecha, fase, limit, offset)
    
    if items is None:
        return {"error": "Error interno al consultar la base de datos", "status_code": 500}

    base_url = "/partidos"
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

    return {
        "items": items,
        "total": total,
        "_links": _links,
        "status_code": 200
    }