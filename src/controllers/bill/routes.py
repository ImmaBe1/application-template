from flask import request, jsonify, Blueprint
from http import HTTPStatus

bill = Blueprint('bill', __name__, url_prefix='/billing')

@bill.route('/pay')
def pay():
    return 'pay a bill'

@bill.route('/view')
def view():
    return 'view a bill'
