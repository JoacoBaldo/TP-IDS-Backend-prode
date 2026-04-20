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

    return {"data": data}
