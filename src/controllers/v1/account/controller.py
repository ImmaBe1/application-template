from src.controllers import json_template_response, logger
from src.models import ModelService

#from src.services.model import ModelService
#from os import environ as env, path

def view_user(username:str) -> dict:
    json_response = json_template_response.copy()
    try:
        json_response['data'] = ModelService.testdboperation("873d5edb06131e7c39b9a8f50070351f")
        json_response['success'] = True
    except Exception as ex:
        json_response["error"] = "Error occurred: {}".format(ex)
        json_response['success'] = False
        logger.error(json_response["error"])
    finally:
        return json_response

def login_user(username:str, password:str) -> dict:
    json_response = json_template_response.copy()
    try:
        json_response['data'] = {"test":"yay!!", "user": username, "password": password}
        json_response['count'] = 2
        json_response['success'] = True
    except Exception as ex:
        json_response["error"] = "Error occurred: {}".format(ex)
        json_response['success'] = False
    finally:
        return json_response

def register_user(user_info:dict) -> dict:
    json_response = json_template_response.copy()
    try:
        json_response['data'] = {"registration": user_info}
        json_response['success'] = True
    except Exception as ex:
        json_response["error"] = "Error occurred: {}".format(ex)
        json_response['success'] = False
    finally:
        return json_response