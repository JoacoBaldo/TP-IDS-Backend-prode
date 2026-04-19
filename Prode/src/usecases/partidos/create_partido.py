from datetime import datetime, timezone
from contracts.response.partidos_response import partido_detalle_response
from infrastructure.errors.partidos import (
    ErrEquipoVacio,
    ErrFaseVacia,
    ErrFechaInvalida,
    ErrReemplazoCamposFaltantes,
)
from repository.partidos.create_fixture_repo import create_fixture_repo

def execute(payload: dict) -> dict:

    if not payload:
        return ErrReemplazoCamposFaltantes

    campos = ["equipo_local", "equipo_visitante", "fecha", "fase"]
    for c in campos:
        if c not in payload:
            return ErrReemplazoCamposFaltantes

    equipo_local = str(payload["equipo_local"]).strip()
    equipo_visitante = str(payload["equipo_visitante"]).strip()
    fecha = str(payload["fecha"]).strip()
    fase = str(payload["fase"]).strip()

    if equipo_local == "" or equipo_visitante == "":
        return ErrEquipoVacio
    if fase == "" or fecha == "":
        return ErrFaseVacia 

    if fecha.endswith("Z"):
        fecha = fecha[:-1] + "+00:00"
    try:
        fecha_dt = datetime.fromisoformat(fecha)
    except ValueError:
        return ErrFechaInvalida

    if fecha_dt.tzinfo is not None:
        fecha_dt = fecha_dt.astimezone(timezone.utc).replace(tzinfo=None)

    nuevo_partido, err = create_fixture_repo(equipo_local, equipo_visitante, fecha_dt, fase)

    if err is not None:
        return err

    nuevo_partido["local_team"] = equipo_local
    nuevo_partido["visitor_team"] = equipo_visitante
    nuevo_partido["date_time"] = fecha_dt
    nuevo_partido["phase"] = fase

    return partido_detalle_response(nuevo_partido, 201)