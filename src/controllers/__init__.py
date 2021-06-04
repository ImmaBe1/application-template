from flask import Flask
app = Flask(__name__)

# Setup Logging 
from src.services.logger import ApiLogger
apilogger = ApiLogger()
apilogger.setupLogger()
logger = apilogger.getLogger()

# Common template for json response
json_template_response = {
    'success': False,
    'data': {},
    'error': ""
}

#Setup JWT
from flask_jwt_extended import JWTManager
from os import environ as env
app.config["JWT_SECRET_KEY"] = env["JWT_SECRET_KEY"]
jwt = JWTManager(app)

#Register v1's blueprints
from os.path import dirname, abspath
base_folder = dirname(dirname(dirname(abspath(__file__)))) #<---used in the openapi middleware for swagger

from src.controllers.v1.account.routes import v1_account
app.register_blueprint(v1_account)

from src.controllers import error_controller