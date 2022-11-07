from flask import render_template, Blueprint
home = Blueprint("home", __name__, template_folder="templates", 
static_folder="static")

@home.route("/")
def index():
    return render_template("home/home.html")