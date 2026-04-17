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

    if "equipo_local" not in payload:
        return ErrReemplazoCamposFaltantes
    if "equipo_visitante" not in payload:
        return ErrReemplazoCamposFaltantes
    if "fecha" not in payload:
        return ErrReemplazoCamposFaltantes
    if "fase" not in payload:
        return ErrReemplazoCamposFaltantes

    equipo_local = payload["equipo_local"]
    equipo_visitante = payload["equipo_visitante"]
    fecha = payload["fecha"]
    fase = payload["fase"]

    if type(equipo_local) is not str or type(equipo_visitante) is not str:
        return ErrEquipoVacio
    if type(fase) is not str:
        return ErrFaseVacia

    equipo_local = equipo_local.strip()
    equipo_visitante = equipo_visitante.strip()
    fase = fase.strip()

    if equipo_local == "" or equipo_visitante == "":
        return ErrEquipoVacio
    if fase == "":
        return ErrFaseVacia

    if type(fecha) is not str:
        return ErrFechaInvalida

    fecha = fecha.strip()
    if fecha == "":
        return ErrFechaInvalida

    if fecha.endswith("Z"):
        fecha = fecha[:-1] + "+00:00"

    try:
        fecha_dt = datetime.fromisoformat(fecha)
    except ValueError:
        return ErrFechaInvalida

    if fecha_dt.tzinfo is not None:
        fecha_dt = fecha_dt.astimezone(timezone.utc).replace(tzinfo=None)

    err = replace_fixture_core(
        fixture_id, equipo_local, equipo_visitante, fecha_dt, fase
    )
    if err is not None:
        return err

    partido = get_fixture_by_id(fixture_id)
    if partido is None:
        return ErrPartidoNotFound

    return partido_detalle_response(partido, 200)
