import logging
from datetime import datetime

class LogGen:

    @staticmethod
    def loggen():
        time = str(datetime.now())
        logging.basicConfig(filename="Logs/log.log")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        print(logger)
        print("inside logger gen")
        return logger