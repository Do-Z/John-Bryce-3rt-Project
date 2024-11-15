from flask import Blueprint, render_template, redirect, url_for, request, session
from facades.auth_facade import AuthFacade
from models.client_error import ValidationError, AuthError
from models.role_model import RoleModel

auth_blueprint = Blueprint("auth_view", __name__)

facade = AuthFacade()

@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "GET": return render_template("register.html", active="register", user={})
        facade.register()
        return redirect(url_for("vacations_view.vacations"))
    except ValidationError as err:
        return render_template("register.html", error = err.message, user = err.model)
    

@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "GET":
            session.clear() # when you go from the url to login page, you logging out.
            err = request.args.get("error")
            return render_template("login.html", error = err, credentials={})
        facade.login()
        user = session.get("current_user")
        if user["role_id"] == RoleModel.User.value: # based on role_id, redirecting to the relevant page
            return redirect(url_for("vacations_view.vacations"))
        return redirect(url_for("vacations_view.admin"))
    except (ValidationError, AuthError) as err:
        return render_template("login.html", error = err.message, credentials = err.model)
    
@auth_blueprint.route("/logout")
def logout():
    try:
        facade.block_anonymous()
        facade.logout()
        return redirect(url_for("auth_view.login"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))