from infrastructure.errors.partidos import ErrPartidoIdInvalido
from repository.partidos.delete_fixture import delete_fixture


def execute(fixture_id: int) -> dict:
    if fixture_id < 1:
        return ErrPartidoIdInvalido

    err = delete_fixture(fixture_id)
    if err is not None:
        return err

    return {"message": "El partido se eliminó correctamente", "status_code": 200}
