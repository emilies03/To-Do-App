import logging
from todo_app.data.constants import LOGGER_NAME

LOGGER_NAME = "todo_app"

def logInfo(message):
    logger = logging.getLogger(LOGGER_NAME)
    logger.info(message)