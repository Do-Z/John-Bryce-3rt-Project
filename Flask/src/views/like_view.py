from flask import Blueprint, redirect, url_for, render_template
from facades.like_facade import LikesFacade
from facades.auth_facade import AuthFacade
from models.client_error import AuthError, ResourceNotFoundError

like_blueprint=Blueprint("like_view", __name__)
@like_blueprint.route("/like/<int:vacation_id>")
def handle_like(vacation_id):
    try:
        auth_facade = AuthFacade()
        like_facade = LikesFacade()
        auth_facade.block_admin()
        auth_facade.block_anonymous()
        like_facade.handle_like(vacation_id)
        return redirect(url_for("vacations_view.vacations"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    except ResourceNotFoundError as err:
        return render_template("404.html", error=err.message)
