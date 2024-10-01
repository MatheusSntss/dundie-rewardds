import logging.handlers
import os 
import logging

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger("dundie")

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'i:%(lineno)d f:%(filename)s: %(message)s'
    )

def get_logger(log_file="dundie.log"):    
    fh = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=300,
        backupCount=10
    )
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log