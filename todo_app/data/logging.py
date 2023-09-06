import logging

LOGGER_NAME = "todo_app"

def getLogger():
    return logging.getLogger(LOGGER_NAME)

def logInfo(message):
    logger = getLogger()
    logger.info(message)

def logError(message):
    logger = getLogger()
    logger.error(message)