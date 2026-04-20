import math
from urllib.parse import urlencode


def ranking_list_response(
    rows: list[dict],
    total: int,
    limit: int,
    offset: int,
    base_url: str,
) -> dict:
    data = [
        {"id_usuario": int(row["id_usuario"]), "puntos": int(row["puntos"])}
        for row in rows
    ]

    def link(off: int) -> str:
        q = urlencode({"limit": limit, "offset": max(0, off)})
        return f"{base_url}?{q}"

    last_offset = 0
    if limit > 0 and total > 0:
        last_offset = max(0, (math.ceil(total / limit) - 1) * limit)

    prev_offset = max(0, offset - limit)
    next_offset = offset + limit

    links = {
        "first": link(0),
        "prev": link(prev_offset) if offset > 0 else link(0),
        "next": link(next_offset) if next_offset < total else link(last_offset),
        "last": link(last_offset),
    }

    return {"data": data, "links": links}
