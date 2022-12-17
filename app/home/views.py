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

@home.route('/search', methods=['GET'])
def search():
    return render_template("home/search.html")

@home.route('/about2', methods=['GET'])
def about2():
    return render_template("home/about2.html")

@home.route('/about3', methods=['GET'])
def about3():
    return render_template("home/about3.html")