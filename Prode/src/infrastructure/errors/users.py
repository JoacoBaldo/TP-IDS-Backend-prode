ErrEmailAlreadyExists: dict  = {"error": "Email already exists", "status_code": 400}
ErrMissingInformation: dict = {"error": "Missing email, name or password", "status_code": 400}
ErrPasswordTooShort: dict = {"error": "Password must be at least 6 characters long", "status_code": 400}
ErrInvalidEmailFormat: dict = {"error": "Invalid email format", "status_code": 400}