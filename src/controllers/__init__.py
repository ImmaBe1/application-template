from flask import Flask
from os.path import dirname, abspath
base_folder = dirname(dirname(dirname(abspath(__file__))))

from src.controllers.site.routes import site
from src.controllers.account.routes import account
from src.controllers.request.routes import request
from src.controllers.bill.routes import bill

app = Flask(__name__,
            static_url_path='/static/',
            static_folder=base_folder + '/src/web/static',
            template_folder=base_folder + '/src/web/templates')

# Get the blueprints to work
app.register_blueprint(site)
app.register_blueprint(account)
app.register_blueprint(request)
app.register_blueprint(bill)

# setup session management
'''
from flask_session import Session
sess = Session()
sess.init_app(app)
'''
app.secret_key = b'7gp3V!2anxCUsbiKlXU' 

# Setup Logging
from src.services.logger import ApiLogger
apilogger = ApiLogger()
apilogger.setupLogger()
apilogger.getLogger()

# Common template for json response
json_template_response = {
    'success': False,
    'data': {},
    'error': {}
}

from src.controllers import error_controller