import logging
import os
from loggly.handlers import HTTPSHandler
from logging import Formatter, StreamHandler

LOGGER_NAME = "todo_app"

def setupLogger():
    streamHandler = StreamHandler()

    handlers = [streamHandler]
    if os.getenv("LOGGLY_TOKEN") is not None:
        logglyHandler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{os.getenv("LOGGLY_TOKEN")}/tag/todo-app')
        logglyHandler.setFormatter(Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s"))
        handlers.append(logglyHandler)

    logLevel = os.environ.get('LOG_LEVEL')
    if logLevel == None :
        logLevel = "INFO"
    
    logging.basicConfig(level = logLevel, handlers= handlers)

def getLogger():
    return logging.getLogger(LOGGER_NAME)

def logInfo(message):
    logger = getLogger()
    logger.info(message)

def logError(message):
    logger = getLogger()
    logger.error(message)