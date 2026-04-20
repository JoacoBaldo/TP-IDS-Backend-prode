_DEFAULT_LIMIT = 20
_MAX_LIMIT = 100


def ranking_list_params(args) -> dict:
    raw_limit = args.get("limit")
    raw_offset = args.get("offset")

    if raw_limit is None or raw_limit == "":
        limit = _DEFAULT_LIMIT
    else:
        try:
            limit = int(raw_limit)
        except ValueError:
            return {"ok": False}

    if raw_offset is None or raw_offset == "":
        offset = 0
    else:
        try:
            offset = int(raw_offset)
        except ValueError:
            return {"ok": False}

    return {
        "ok": True,
        "limit": limit,
        "offset": offset,
        "max_limit": _MAX_LIMIT,
    }
