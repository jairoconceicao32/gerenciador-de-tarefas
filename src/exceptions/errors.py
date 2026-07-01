class CustomError(Exception):
    pass

class ValidationError(CustomError):
    pass

class InvalidNameError(ValidationError):
    pass

class InvalidDescriptionError(ValidationError):
    pass

class InvalidDeadlineError(ValidationError):
    pass

class InvalidTaskidError(ValidationError):
    pass

class DatabaseError(CustomError):
    pass

class NotFoundError(CustomError):
    pass

