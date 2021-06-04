from flask import request, jsonify, Blueprint

request = Blueprint('request', __name__, url_prefix='/requests')

@request.route('/')
def show_all__requests():
    return 'These are my requests'

@request.route('/view')
def view_a_request():
    return 'View a specific request'

@request.route('/cancel')
def cancel_a_request():
    return 'Tell us why you are canceling this request'