from flask import Flask, Response, jsonify, make_response, render_template, Blueprint
from flask_pymongo import PyMongo
import sys

import app
from app import app as flask_app

# flask_app = Flask(__name__)

flask_app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/hospital_db"
flask_app.config["EXPLAIN_TEMPLATE_LOADING"] = True
mongo = PyMongo(flask_app)
mongo_db = mongo.db

# @app.route('/home')
# def hello():
#     return 'home'
#     return render_template('home/home.html', template_folder='/home/ubuntu/wangswift/FlaskNginx/app/templates')


if __name__ == "__main__":
    flask_app.run(host="127.0.0.1", port='8001')
