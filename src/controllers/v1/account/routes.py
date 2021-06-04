
'''
Make sure all the required environment variables are present
'''
#from src.services.validator import check_environment
#from os import environ as path 
#check_environment(path.basename(__file__))

'''
Import packages and modules
'''
from http import HTTPStatus 
from flask import Blueprint, request, jsonify
import src.controllers.v1.account.controller as controller
from src.middlewares.flasgger import openapi_path
from src.middlewares.auth import rbac_required
from .authorization_map import auth_roles
from flasgger import swag_from

v1_account = Blueprint('v1_account', __name__, url_prefix='/v1/account')

'''
This is sample creation fxn of jwt token that must be used by the ui server 
to create valid jwt token that it will use to consume api endpoints.
Uncomment it if you want to generate a jwt token to test the api.
'''
'''
from flask_jwt_extended import create_access_token
@v1_account.route("/jwt-token", methods=["GET"])
def sample():
    username = {"userxxxx":"myusername", "roles":["myrole", "role2"]}
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
'''

@v1_account.route('/view', methods=['GET'])
@v1_account.route('/view/<string:username>', methods=['GET'])
@swag_from("{}/v1/view.yml".format(openapi_path))
@rbac_required(auth_roles["view"])
def view_user(username:str=""): 
    """
    Public endpoint to load the profile info of a user. 

    :param username: (optional) username of the user.
    :type source: str

    :returns: Json response data and response code.
    :rtype: flask.Response, int
    """
    response = controller.view_user(username)
    
    if len(response["error"]) > 0:
        return jsonify(response), HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        return jsonify(response), HTTPStatus.OK


@v1_account.route('/login', methods=['POST'])
#@swag_from("{}/v1/login.yml".format(openapi_path))
def login_user(): 
    """
    Public endpoint for log in a user.   

    :param next: The username of the visitor.
    :type source: str
    :param next: The password of the visitor.
    :type source: str

    :returns: Json response data and response code.
    :rtype: flask.Response, int
    """
    try: 
        username = request.values.get('username')
        password = request.values.get('password')

        response = controller.login_user(username, password)
        
        if len(response["error"]) > 0:
            return jsonify(response), HTTPStatus.INTERNAL_SERVER_ERROR
        else:
            return jsonify(response), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":e, "debug": "Make sure you are sending the username and the password"}), HTTPStatus.BAD_REQUEST


@v1_account.route('/register', methods=['POST'])
#@swag_from("{}/v1/register.yml".format(openapi_path))
def register_user(): 
    """
    Public endpoint for register a user. 

    :param ...: The set of required info about the user.
    :type source: dict

    :returns: Json response data and response code.
    :rtype: flask.Response, int
    """
    try:
        username = request.values.get('username')
        fullname = request.values.get('name')
        password = request.values.get('password')

        response = controller.register_user({"username":username, "fullname": fullname, "password":password})

        if response["success"] == True:
            return jsonify(response), HTTPStatus.OK
        else:
            return jsonify(response), HTTPStatus.INTERNAL_SERVER_ERROR
    except Exception as e:
        return jsonify({"error":e, "debug": "Make sure you are sending the right user info"}), HTTPStatus.BAD_REQUEST