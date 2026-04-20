ErrPartidoNotFound: dict = {"error": "Partido no encontrado", "status_code": 404}
ErrPartidoIdInvalido: dict = {"error": "Identificador de partido inválido", "status_code": 400}
ErrResultadoCamposFaltantes: dict = {
    "error": "goles_local y goles_visitante son obligatorios",
    "status_code": 400,
}
ErrGolesInvalidos: dict = {"error": "Los goles deben ser enteros mayores o iguales a cero", "status_code": 400}
ErrReemplazoCamposFaltantes: dict = {
    "error": "equipo_local, equipo_visitante, fecha y fase son obligatorios",
    "status_code": 400,
}
ErrEquipoVacio: dict = {"error": "Los nombres de equipo no pueden estar vacíos", "status_code": 400}
ErrFechaInvalida: dict = {"error": "fecha debe ser una fecha y hora ISO 8601 válida", "status_code": 400}
ErrFaseVacia: dict = {"error": "fase no puede estar vacía", "status_code": 400}

ErrMissingFields: dict = {"error": "id_usuario, local y visitante son obligatorios", "status_code": 400}
ErrInvalidFieldType: dict = {"error": "id_usuario, local y visitante deben ser enteros", "status_code": 400}
ErrInvalidGoals: dict = {"error": "Los goles deben ser mayores o iguales a cero", "status_code": 400}
ErrUserNotFound: dict = {"error": "Usuario no encontrado", "status_code": 404}
ErrPartidoAlreadyPlayed: dict = {"error": "El partido ya se ha jugado", "status_code": 400}
ErrPredictionAlreadyExists: dict = {"error": "El usuario ya tiene una predicción para este partido", "status_code": 409}
