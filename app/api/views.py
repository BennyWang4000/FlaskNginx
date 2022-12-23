from flask import render_template, Blueprint, make_response, jsonify, request
import sys
from datetime import date, datetime
from db.accessor import hosp_accessor
import config as cfg
import json

api = Blueprint("api", __name__,)

hosp = hosp_accessor.HospAccessor(host=cfg.host, user=cfg.user,
                    database=cfg.database, password=cfg.password)

@api.route('/select_dep', methods=['POST'])
def select_dep():
    result = hosp.select_dep()
    response = make_response(jsonify({"content": result}), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@api.route('/select_doc', methods=['POST'])
def select_doc():
    request_data = request.get_json()
    dep_id = request_data['dep_id']
    result = hosp.select_doc(dep_id)
    response = make_response(jsonify({"content": result}), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@api.route('/select_cli', methods=['POST'])
def select_cli():
    request_data = request.get_json()
    doc_id= request_data['doc_id']
    result = hosp.select_cli(doc_id)
    response = make_response(json.dumps({"content": result}, default=str), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@api.route('/select_app', methods=['POST'])
def select_app():
    request_data = request.get_json()
    med_id, pat_date = request_data['med_id'], request_data['pat_date']
    result = hosp.select_app(med_id, pat_date)
    response = make_response(json.dumps({"content": result}, default=str), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@api.route('/insert_app', methods=['POST'])
def insert_app():
    request_data = request.get_json()
    med_id, cli_id = request_data['med_id'], request_data['cli_id']
    result = hosp.insert_app(med_id, cli_id)
    response = make_response(jsonify({}), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@api.route('/complete_app', methods=['POST'])
def complete_app():
    request_data = request.get_json()
    med_id, cli_id = request_data['med_id'], request_data['cli_id']
    result = hosp.complete_app(med_id, cli_id)
    response = make_response(jsonify({}), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@api.route('/cancel_app', methods=['POST'])
def cancel_app():
    request_data = request.get_json()
    med_id, cli_id = request_data['med_id'], request_data['cli_id']
    result = hosp.cancel_app(med_id, cli_id)
    response = make_response(jsonify({}), 200)
    response.headers["Content-Type"] = "application/json"
    return response

