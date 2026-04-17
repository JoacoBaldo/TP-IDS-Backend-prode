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

    if "goles_local" not in payload or "goles_visitante" not in payload:
        return ErrResultadoCamposFaltantes

    goles_local = payload["goles_local"]
    goles_visitante = payload["goles_visitante"]

    if type(goles_local) is not int or type(goles_visitante) is not int:
        return ErrGolesInvalidos

    if goles_local < 0 or goles_visitante < 0:
        return ErrGolesInvalidos

    err = update_fixture_goals(fixture_id, goles_local, goles_visitante)
    if err is not None:
        return err

    partido = get_fixture_by_id(fixture_id)
    if partido is None:
        return ErrPartidoNotFound

    return partido_detalle_response(partido, 200)
