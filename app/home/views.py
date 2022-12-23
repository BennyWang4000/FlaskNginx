from flask import render_template, Blueprint, request

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

@home.route('/about2', methods=['GET'])
def about2():
    dep_id, dep_name= request.args.get('dep_id'), request.args.get('dep_name')
    return render_template("home/about2.html", dep_id=dep_id, dep_name=dep_name)

@home.route('/about3', methods=['GET'])
def about3():
    doc_id, doc_name= request.args.get('doc_id'), request.args.get('doc_name')
    return render_template("home/about3.html", doc_id=doc_id, doc_name=doc_name)

@home.route('/search', methods=['GET'])
def search():
    return render_template("home/search.html")

@home.app_errorhandler(Exception)
def handle_exception(err):
    return render_template('error/exception.html', err=err)
