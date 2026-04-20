from datetime import datetime, timezone

from contracts.response.partidos_response import partido_detalle_response
from infrastructure.errors.partidos import (
    ErrEquipoVacio,
    ErrFaseVacia,
    ErrFechaInvalida,
    ErrPartidoIdInvalido,
    ErrPartidoNotFound,
    ErrReemplazoCamposFaltantes,
)
from repository.partidos.get_fixture_by_id import get_fixture_by_id
from repository.partidos.replace_fixture_core import replace_fixture_core


def execute(fixture_id: int, payload: dict) -> dict:
    if fixture_id < 1:
        return ErrPartidoIdInvalido

    if not payload:
        return ErrReemplazoCamposFaltantes

    required_fields = ["local_team", "visitor_team", "date_time", "phase"]
    for field_name in required_fields:
        if field_name not in payload:
            return ErrReemplazoCamposFaltantes

    local_team = payload["local_team"]
    visitor_team = payload["visitor_team"]
    date_time_raw = payload["date_time"]
    phase = payload["phase"]

    if type(local_team) is not str or type(visitor_team) is not str:
        return ErrEquipoVacio
    if type(phase) is not str:
        return ErrFaseVacia

    local_team = local_team.strip()
    visitor_team = visitor_team.strip()
    phase = phase.strip()

    if local_team == "" or visitor_team == "":
        return ErrEquipoVacio
    if phase == "":
        return ErrFaseVacia

    if type(date_time_raw) is not str:
        return ErrFechaInvalida

    date_time_raw = date_time_raw.strip()
    if date_time_raw == "":
        return ErrFechaInvalida

    if date_time_raw.endswith("Z"):
        date_time_raw = date_time_raw[:-1] + "+00:00"

    try:
        date_time = datetime.fromisoformat(date_time_raw)
    except ValueError:
        return ErrFechaInvalida

    if date_time.tzinfo is not None:
        date_time = date_time.astimezone(timezone.utc).replace(tzinfo=None)

    err = replace_fixture_core(
        fixture_id, local_team, visitor_team, date_time, phase
    )
    if err is not None:
        return err

    partido = get_fixture_by_id(fixture_id)
    if partido is None:
        return ErrPartidoNotFound

    return partido_detalle_response(partido, 200)
