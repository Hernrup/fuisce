import logging
import sys

class Log:

    logger = None

    def __init__(self):
        global logger

        # logger
        logger = logging.getLogger(__name__)
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        root.addHandler(ch)

    def instance(self):
       global logger
       return logger