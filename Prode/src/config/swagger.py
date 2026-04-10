from flasgger import Swagger

def init_swagger(app):
    """
    Inicializa Flasgger con configuración para generar documentación OpenAPI
    sin exponer la UI pública
    """
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": False,  # Deshabilitar UI pública
        "specs_route": "/docs/"  # Ruta para especificaciones (no accesible públicamente)
    }
    
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "TP Backend API",
            "description": "API para el TP de Introducción al Desarrollo de Software",
            "version": "1.0.0"
        },
        "host": "localhost:5000",
        "basePath": "/",
        "schemes": ["http"],
        "consumes": [
            "application/json"
        ],
        "produces": [
            "application/json"
        ],
        "definitions": {
            "User": {
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "format": "email",
                        "example": "test@example.com"
                    },
                    "password": {
                        "type": "string",
                        "minLength": 6,
                        "example": "password123"
                    }
                },
                "required": ["email", "password"]
            },
            "UserResponse": {
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "example": "test@example.com"
                    },
                    "message": {
                        "type": "string",
                        "example": "User created successfully"
                    },
                    "status_code": {
                        "type": "integer",
                        "example": 201
                    }
                }
            },
            "ErrorResponse": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "example": "Error message"
                    }
                }
            }
        }
    }
    
    return Swagger(app, config=swagger_config, template=swagger_template)

def get_openapi_spec(app):
    """
    Obtiene la especificación OpenAPI completa para uso interno
    """
    with app.app_context():
        return app.config.get('SWAGGER', {}).get('spec', {})
