from datetime import datetime, timezone
from contracts.response.partidos_response import partido_detalle_response
from infrastructure.errors.partidos import (
    ErrEquipoVacio,
    ErrFaseVacia,
    ErrFechaInvalida,
    ErrReemplazoCamposFaltantes,
)
from repository.partidos.create_fixture_repo import create_fixture

def execute(payload: dict) -> dict:

    if not payload:
        return ErrReemplazoCamposFaltantes

    required_fields = ["local_team", "visitor_team", "date_time", "phase"]
    for field_name in required_fields:
        if field_name not in payload:
            return ErrReemplazoCamposFaltantes

    local_team = str(payload["local_team"]).strip()
    visitor_team = str(payload["visitor_team"]).strip()
    date_time_raw = str(payload["date_time"]).strip()
    phase = str(payload["phase"]).strip()

    if local_team == "" or visitor_team == "":
        return ErrEquipoVacio
    if phase == "" or date_time_raw == "":
        return ErrFaseVacia 

    if date_time_raw.endswith("Z"):
        date_time_raw = date_time_raw[:-1] + "+00:00"
    try:
        date_time = datetime.fromisoformat(date_time_raw)
    except ValueError:
        return ErrFechaInvalida

    if date_time.tzinfo is not None:
        date_time = date_time.astimezone(timezone.utc).replace(tzinfo=None)

    new_fixture, err = create_fixture(
        {
            "local_team": local_team,
            "visitor_team": visitor_team,
            "date_time": date_time,
            "phase": phase,
        }
    )

    if err is not None:
        return err

    new_fixture["local_team"] = local_team
    new_fixture["visitor_team"] = visitor_team
    new_fixture["date_time"] = date_time
    new_fixture["phase"] = phase

    return partido_detalle_response(new_fixture, 201)