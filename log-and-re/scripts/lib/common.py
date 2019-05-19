from conf.settings import LOGGING_DIC
import logging.config
logging.config.dictConfig(LOGGING_DIC)

def getLogger(name):
    return logging.getLogger(name)