import logging
import os
from loggly.handlers import HTTPSHandler
from logging import Formatter, StreamHandler

LOGGER_NAME = "todo_app"

def setupLogger():
    streamHandler = StreamHandler()
    logglyHandler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{os.getenv("LOGGLY_TOKEN")}/tag/todo-app')
    logglyHandler.setFormatter(Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s"))
    
    logging.basicConfig(level = os.getenv('LOG_LEVEL'), handlers= [streamHandler, logglyHandler])

def getLogger():
    return logging.getLogger(LOGGER_NAME)

def logInfo(message):
    logger = getLogger()
    logger.info(message)

def logError(message):
    logger = getLogger()
    logger.error(message)