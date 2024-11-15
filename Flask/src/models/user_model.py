#pip install email-validator
from validate_email_address import validate_email
from models.role_model import RoleModel

class UserModel:
    # initiating the registered user
    def __init__(self, user_id, first_name, last_name, email, password, role_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id
    
    # validating the registration data
    def validate_insert(self):
        if not self.first_name: return "missing first name"
        if not self.last_name: return "missing last name"
        if not self.email: return "missing email"
        if not self.password: return "missing password"
        if len(self.password) < 4: return "password must be longer than 4 chars"
        if len(self.first_name) < 2 or len(self.first_name) > 20: return "first name must be 2-20"
        if len(self.last_name) < 2 or len(self.last_name) > 20: return "last name must be 2-20"
        if not validate_email(self.email): return "email is not valid"
        if self.role_id != RoleModel.Admin.value and self.role_id!=RoleModel.User.value : "not valid role"
        return None     