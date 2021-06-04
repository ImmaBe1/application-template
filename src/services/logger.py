import logging
import logging.handlers
from os import environ as env
from src.services.util import Auxil

# Set logging file bytes to 1GB
MAX_FILE_BYTES = 1000000000

class ApiLogger:
    def __init__(self):
        self.logger = None
    
    def setupLogger(self):
        Auxil.create_directory(env['LOG_DIR'])
        log_file_path = "{}/{}".format(env['LOG_DIR'], env['LOG_FILE'])
        #Create and configure logger 
        self.logger = logging.getLogger()
        # Add the log message handler to the logger
        handler = logging.handlers.RotatingFileHandler(
                log_file_path, maxBytes=MAX_FILE_BYTES, backupCount=10)
        
        formatter  = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
    
    def getLogger(self):
        return self.logger
