from contracts.response.partidos_response import partido_detalle_response
from infrastructure.errors.partidos import (
    ErrGolesInvalidos,
    ErrPartidoIdInvalido,
    ErrPartidoNotFound,
    ErrResultadoCamposFaltantes,
)
from repository.partidos.get_fixture_by_id import get_fixture_by_id
from repository.partidos.update_fixture_goals import update_fixture_goals


def execute(fixture_id: int, payload: dict) -> dict:
    if fixture_id < 1:
        return ErrPartidoIdInvalido

    if not payload:
        return ErrResultadoCamposFaltantes

    if "local_goals" not in payload or "visitor_goals" not in payload:
        return ErrResultadoCamposFaltantes

    local_goals = payload["local_goals"]
    visitor_goals = payload["visitor_goals"]

    if type(local_goals) is not int or type(visitor_goals) is not int:
        return ErrGolesInvalidos

    if local_goals < 0 or visitor_goals < 0:
        return ErrGolesInvalidos

    err = update_fixture_goals(fixture_id, local_goals, visitor_goals)
    if err is not None:
        return err

    partido = get_fixture_by_id(fixture_id)
    if partido is None:
        return ErrPartidoNotFound

    return partido_detalle_response(partido, 200)
