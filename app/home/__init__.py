from flask import render_template, Blueprint
from . import views

home = Blueprint("home", __name__,
                 template_folder="templates",
                 static_folder="static",
                 static_url_path='/home/static')


@home.route("/")
def index():
    return render_template("home/home.html")
