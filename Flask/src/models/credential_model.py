from email_validator import validate_email

# model used for logging in
class CredentialModel:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate(self):
        if not self.email: return "One of the parameters is wrong"
        if not self.password: return "One of the parameters is wrong"
        if not validate_email(self.email): return "One of the parameters is wrong"
        return None