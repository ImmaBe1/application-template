from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import jsonify
from http import HTTPStatus
from functools import wraps


def rbac_required(groups:list):
    """
    Decorator function to provide access an endpoint if the user is included in an access group.
    Must pass a JWT Authorization token in the header with the key "Bearer" to authenticate.

    :param groups: List of bluegroups that person must be apart of to have access,
    :type groups: list
    :param func: Top level parameter function to decorate.
    :type func: Callable
    :param *args: Non keyword arguments passed in func.
    :type args: list
    :param **kwargs: Keyword arguments passed in func.
    :type **kwargs: list

    :returns: Top level parameter function or data returning an error
    :type: (Callable, dict)
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            
            if 'sub' in claims and 'roles' in claims['sub'] and any((True for x in groups if x in claims['sub']['roles'])):
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), HTTPStatus.FORBIDDEN
        return decorator

    return wrapper