from flask import Blueprint, render_template, redirect, url_for, request, send_file, session
from facades.vacation_facade import VacationFacade
from utils.image_handler import ImageHandler
from models.client_error import ValidationError, AuthError, ResourceNotFoundError
from facades.auth_facade import AuthFacade
from utils.flag_handler import FlagHandler

vacations_blueprint = Blueprint("vacations_view", __name__)
vacation_facade = VacationFacade()
auth_facade = AuthFacade()

@vacations_blueprint.route("/vacations/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)

@vacations_blueprint.route("/vacations")
def vacations():
    try:
        err = request.args.get("error")
        auth_facade.block_anonymous()
        auth_facade.block_admin()
        all_vacations = vacation_facade.get_all_vacations()
        liked_vacations_ids = vacation_facade.get_liked_vacations_ids()
        return render_template("vacations.html", vacations=all_vacations, ids = liked_vacations_ids, error = err, active="vacations")
    except AuthError as err:
        user = session.get("current_user")
        if not user:
            return redirect(url_for("auth_view.login", error = err.message))
        return redirect(url_for("vacations_view.admin", error = err.message))
    
@vacations_blueprint.route("/admin")
def admin():
    try:
        err = request.args.get("error")
        auth_facade.block_anonymous()
        auth_facade.block_non_admin()
        all_vacations = vacation_facade.get_all_vacations()
        return render_template("admin.html", vacations = all_vacations, error = err, active="admin")
    except AuthError as err:
        user = session.get("current_user")
        if not user:
            return redirect(url_for("auth_view.login", error = err.message))
        return redirect(url_for("vacations_view.vacations", error = err.message))

@vacations_blueprint.route("/vacations/new", methods=["GET", "POST"])
def insert():
    try:
        auth_facade.block_anonymous()
        auth_facade.block_non_admin()
        all_countries = vacation_facade.get_all_countries()
        countries_with_flags_classes = FlagHandler.get_countries_with_flags_classes()
        if request.method =="GET":
            return render_template("insert.html", countries = countries_with_flags_classes, active="insert")
        vacation_facade.add_vacation()
        return redirect(url_for("vacations_view.admin"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    except ValidationError as err:
        return render_template("insert.html",error=err.message, countries = all_countries, active = "insert")

@vacations_blueprint.route("/vacations/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    try:
        auth_facade.block_anonymous()
        auth_facade.block_non_admin()
        if request.method == "GET":
            one_vacation = vacation_facade.get_one_vacation(id)
            countries_with_flags_classes = FlagHandler.get_countries_with_flags_classes()
            return render_template("edit.html", vacation=one_vacation, countries=countries_with_flags_classes, active="edit")
        vacation_facade.update_vacation()
        return redirect(url_for("vacations_view.admin"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    except ResourceNotFoundError as err:
        return render_template("404.html", error=err.message)
    except ValidationError as err:
        return render_template("edit.html",error=err.message, vacation=err.model)

@vacations_blueprint.route("/vacations/delete/<int:id>")
def delete(id):
    auth_facade.block_anonymous()
    auth_facade.block_non_admin()
    try:
        vacation_facade.delete_vacation(id)
        return redirect(url_for("vacations_view.admin"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    except ResourceNotFoundError as err:
        return render_template("404.html", error=err.message)
    