from flask import Flask, render_template
from views.home_view import home_blueprint
from views.vacations_view import vacations_blueprint
from views.auth_view import auth_blueprint
from views.like_view import like_blueprint
from utils.app_config import AppConfig

app = Flask(__name__)
app.register_blueprint(home_blueprint)
app.register_blueprint(vacations_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(like_blueprint)
app.secret_key = AppConfig.session_secret_key

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.errorhandler(Exception)
def catch_all(error):
    return render_template('500.html', error=error)