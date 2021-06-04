from src.controllers import app
import os

if __name__ == '__main__':
    app.debug = os.environ["DEBUG"]
    app.run(host=os.environ["FLASK_RUN_HOST"], port=os.environ["FLASK_RUN_PORT"])