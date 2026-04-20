from urllib.parse import urlencode

from repository.partidos.get_matches import get_partidos_repo


def _partidos_query(equipo: str, fecha: str, fase: str, limit: int, offset: int) -> str:
    q = {}
    if equipo:
        q["equipo"] = equipo
    if fecha:
        q["fecha"] = fecha
    if fase:
        q["fase"] = fase
    q["limit"] = limit
    q["offset"] = offset
    return "?" + urlencode(q)


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
        "first": f"{base_url}{_partidos_query(equipo, fecha, fase, limit, 0)}",
        "last": f"{base_url}{_partidos_query(equipo, fecha, fase, limit, last_offset)}",
    }

    if offset > 0:
        prev_offset = max(0, offset - limit)
        _links["prev"] = f"{base_url}{_partidos_query(equipo, fecha, fase, limit, prev_offset)}"

    if (offset + limit) < total:
        next_offset = offset + limit
        _links["next"] = f"{base_url}{_partidos_query(equipo, fecha, fase, limit, next_offset)}"

    return {
        "items": items,
        "total": total,
        "_links": _links,
        "status_code": 200
    }