from flask import Flask, Response, jsonify, make_response, render_template, Blueprint
from flask_pymongo import PyMongo
import sys

from app.views import home 


app = Flask(__name__)
app.register_blueprint(home, url_prefix='/app')

app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/hospital_db"
app.config["EXPLAIN_TEMPLATE_LOADING"] = True
mongo = PyMongo(app)
mongo_db= mongo.db

# @app.route('/home')
# def hello():
#     return 'home'
#     return render_template('home/home.html', template_folder='/home/ubuntu/wangswift/FlaskNginx/app/templates')


@app.route('/insert_appointment', methods=['POST'])
def insert_appointment():
    request_data = request.get_json()
    med_id, cli_id= request_data['med_id'], request_data['cli_id']
    response = make_response(jsonify({"product_List": product_List, "severity": "danger"} ), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/get_appointment', methods=['POST'])
def get_appointment():
    request_data = request.get_json()
    response = make_response(jsonify({"product_List": product_List, "severity": "danger"} ), 200)
    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == "__main__":
    print(app.url_map)
    app.run(host="127.0.0.1", port='8001')