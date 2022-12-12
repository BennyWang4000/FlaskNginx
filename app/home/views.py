from flask import render_template, Blueprint

home = Blueprint("home", __name__,
                 template_folder="templates",
                 static_folder="static",
                 static_url_path='/home/static')


@home.route("/")
def index():
    return render_template("home/home.html")


@home.route('/about', methods=['GET'])
def about():
    return render_template("home/about.html")