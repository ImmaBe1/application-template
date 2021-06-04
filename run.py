from src.controllers import app
from os import environ as env
import datetime

if __name__ == '__main__':
    app.debug = env["DEBUG"]
    app.secret_key = b'{}'.format(env["UI_SESSION_SECRET"])
    app.config['SESSION_TYPE'] = env["UI_SESSION_TYPE"]
    app.config['SESSION_USE_SIGNER'] = True
    app.permanent_session_lifetime = datetime.timedelta(days=env["UI_SESSION_LIFETIME"])
    '''
    app.config['SESSION_MEMCACHED'] = '127.0.0.1:11211'
    '''
    app.run(host=env["FLASK_RUN_HOST"], port=env["FLASK_RUN_PORT"])
