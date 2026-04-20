from contracts.response.partidos_response import partido_detalle_response
from infrastructure.errors.partidos import ErrPartidoIdInvalido, ErrPartidoNotFound
from repository.partidos.get_fixture_by_id import get_fixture_by_id

def execute(fixture_id: int) -> dict:
    
    if fixture_id < 1:
        return ErrPartidoIdInvalido
    
    partido = get_fixture_by_id(fixture_id)
    
    if partido is None:
        return ErrPartidoNotFound
    
    return partido_detalle_response(partido, 200)