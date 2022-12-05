from flask import render_template, Blueprint
home = Blueprint("home", __name__, template_folder="templates", static_folder="static")
# home = Blueprint("home", __name__, template_folder="templates", static_url_path='/static/', static_folder="static")

@home.route("/app")
def index():
    return render_template("/app/home/home.html")