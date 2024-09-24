import os 
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.debug)
logging.FileHandler("meulog.log")