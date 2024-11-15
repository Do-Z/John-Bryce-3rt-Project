class ClientError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ResourceNotFoundError(ClientError):
    def __init__(self, id):
        super().__init__(f"id {id} not found")
        self.id = id

class ValidationError(ClientError):
    def __init__(self, message, model=None): #default model is none, unless one is given
        super().__init__(message)
        self.model = model

class AuthError(ClientError):
    def __init__(self, message, model=None): #default model is none, unless one is given
        super().__init__(message)
        self.model = model