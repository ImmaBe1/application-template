from http import HTTPStatus
#from flask import render_template, jsonify - To use when you want to display the error from an html file
from src.controllers import app

@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(e):
    """
    Error handler for 404 Errors not found.

    :returns: HTML render template or json data with error details and response code.
    :rtype: flask.Response, int
    """
    return 'This page does not exist', HTTPStatus.NOT_FOUND

@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)  
def internal_server_error(e):
    """
    Error handler for 500 Errors for internal server error.

    :returns: HTML render template or json data with error details and response code.
    :rtype: flask.Response, int
    """
    return 'An internal server occured',  HTTPStatus.INTERNAL_SERVER_ERROR

@app.errorhandler(HTTPStatus.UNAUTHORIZED)  
def unauthorized(e):
    """
    Error handler for 401 Errors for unauthorized issues.

    :returns: HTML render template or json data with error details and response code.
    :rtype: flask.Response, int
    """
    return 'You are not authorized to view this page ',  HTTPStatus.UNAUTHORIZED

@app.errorhandler(HTTPStatus.GONE)  
def gone(e):
    """
    Error handler for 410 Errors for dead (idle) user sessions.

    :returns: HTML render template or json data with error details and response code.
    :rtype: flask.Response, int
    """
    return 'This resource is gone',  HTTPStatus.GONE
