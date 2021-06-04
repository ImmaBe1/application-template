import requests
import os
from flask import jsonify, make_response
from os import environ as env

backend_url = env["BACKEND_URL"]

def create_directory(dir_path):
    if os.path.exists(dir_path) == False:
        try:
            os.mkdir(dir_path)
        except OSError:
            print ("Unable to create a directory: %s" % dir_path)
            return False
    return True

def httpQuery(qtype:str, endpoint:str,  data:dict = None, session_data:dict = None) -> any:
    """
    API query utility function.
    
    :param qtype: Type of query performed (post, get, put).
    :type source: str

    :param endpoint: Specific endpoint appended to backend url for querying.
    :type source: str

    :param data: Payload sent to the query.
    :type source: dict

    :param session: Flag to trigger authenticated query.
    :type source: dict (Optional)

    :returns: Json response data and response code.
    :rtype: dict, int
    """  
    api_url = backend_url + endpoint
    try:
        if session_data is not None and 'token' in session_data:
            headers = {
                "APP-ACCESS-TOKEN" : session_data['token'],
                "Content-Type": "application/json"
            }
            if qtype == "post":
                response = requests.post(api_url, data=data, headers=headers, verify=False)
            elif qtype == "get":
                response = requests.get(api_url, params=data, headers=headers, verify=False)
            elif qtype == "put":
                response = requests.put(api_url, data=data, headers=headers, verify=False)
            else:
                return make_response(jsonify({"text": "E1-Unauthorized query method"}), 401)
        else:
            if qtype == "post":
                response = requests.post(api_url, data=data, verify=False)
                print(requests.headers)
            elif qtype == "get":
                response = requests.get(api_url, params=data, verify=False)
            elif qtype == "put":
                response = requests.put(api_url, data=data, verify=False)
            else:
                return make_response(jsonify({"text": "E2-Unauthorized query method"}), 401)
    except Exception as e:
        return make_response(jsonify({"text": "An unexpected error occurred"}), 500)

    return make_response(response.json(), response.status_code)
