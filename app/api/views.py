from flask import render_template, Blueprint

# from db.accessor.hosp_accessor import HospAccessor

api = Blueprint("api", __name__,)


# hosp = HospAccessor(host='host', user='user',
#                     database='database', password='password')


# @api.route('/select_dep', methods=['POST'])
# def select_dep():
#     result = hosp.select_dep()
#     response = make_response(jsonify({"content": result}), 200)
#     response.headers["Content-Type"] = "application/json"
#     return response


# @api.route('/select_doc', methods=['POST'])
# def select_doc():
#     request_data = request.get_json()
#     dep_id = request_data['dep_id']
#     result = hosp.select_doc(dep_id)
#     response = make_response(jsonify({"content": result}), 200)
#     response.headers["Content-Type"] = "application/json"
#     return response


# @api.route('/select_cli', methods=['POST'])
# def select_cli():
#     request_data = request.get_json()
#     doc_id = request_data['doc_id']
#     result = hosp.select_cli(doc_id)
#     response = make_response(jsonify({"content": result}), 200)
#     response.headers["Content-Type"] = "application/json"
#     return response


# @api.route('/select_reg', methods=['POST'])
# def select_reg():
#     request_data = request.get_json()
#     p_id, p_date = request_data['p_id'], request_data['p_date']
#     result = hosp.select_reg(p_id, p_date)
#     response = make_response(jsonify({"content": result}), 200)
#     response.headers["Content-Type"] = "application/json"
#     return response


# @api.route('/insert_reg', methods=['POST'])
# def select_dep():
#     request_data = request.get_json()
#     p_id, p_date = request_data['p_id'], request_data['p_date']
#     result = hosp.insert_reg(p_id, p_date)
#     response = make_response(jsonify({}), 200)
#     response.headers["Content-Type"] = "application/json"
#     return response


# @api.route('/delete_reg', methods=['POST'])
# def delete_reg():
#     request_data = request.get_json()
#     cli_id, p_id = request_data['cli_id'], request_data['p_id']
#     result = hosp.delete_reg(cli_id, p_id)
#     response = make_response(jsonify({}), 200)
#     response.headers["Content-Type"] = "application/json"
#     return response
