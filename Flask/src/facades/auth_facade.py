from logic.auth_logic import AuthLogic
from flask import request, session
from models.user_model import UserModel
from models.role_model import RoleModel
from models.client_error import ValidationError, AuthError
from models.credential_model import CredentialModel
from utils.cyber import Cyber

class AuthFacade:
# initiating the logic field in this class 
    def __init__(self): 
        self.logic = AuthLogic()

# handling registration 
    def register(self): 
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        user = UserModel(None, first_name, last_name, email, password, RoleModel.User.value)
        error = user.validate_insert()
        if error: raise ValidationError(error, user)
        if self.logic.is_email_taken(email): raise ValidationError("Email already exists", user) # user save the details in the fields 
        user.password = Cyber.hash(user.password)
        self.logic.add_user(user)
        user = self.logic.get_user(user.email, user.password)
        session["current_user"] = user

# handling logging in
    def login(self):
        email = request.form.get("email")
        password = request.form.get("password")
        credentials = CredentialModel(email, Cyber.hash(password))
        error = credentials.validate()
        if error: raise ValidationError(error, credentials)
        user = self.logic.get_user(credentials.email, credentials.password)
        if not user: raise AuthError("Incorrect email or password", user)
        session["current_user"] = user

# handling logging out
    def logout(self):
        session.clear()

# blocking not logged in users
    def block_anonymous(self):
        user = session.get("current_user")
        if not user: raise AuthError("You are not logged in")

# blocking regular users
    def block_non_admin(self):
        user = session.get("current_user")
        if user["role_id"] != RoleModel.Admin.value: raise AuthError("You are not allowed")

# blocking admin access
    def block_admin(self):
        user = session.get("current_user")
        if user["role_id"] == RoleModel.Admin.value: raise AuthError("You can not see this page")

# closing
    def close(self):
        self.logic.close()
