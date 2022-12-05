
# @app.route('/insert_appointment', methods=['POST'])
# def insert_appointment():
#     request_data = request.get_json()
#     med_id, cli_id = request_data['med_id'], request_data['cli_id']
#     response = make_response(
#         jsonify({"product_List": product_List, "severity": "danger"}), 200)
#     response.headers["Content-Type"] = "application/json"
#     return response


# @app.route('/get_appointment', methods=['POST'])
# def get_appointment():
#     request_data = request.get_json()
#     response = make_response(
#         jsonify({"product_List": product_List, "severity": "danger"}), 200)
#     response.headers["Content-Type"] = "application/json"
#     return response
