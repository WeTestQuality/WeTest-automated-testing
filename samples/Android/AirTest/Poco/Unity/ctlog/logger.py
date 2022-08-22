# -*- coding: UTF-8 -*-
import logging
import os


def init_logger():
    handler = logging.StreamHandler()
    fmt = '%(asctime)s - %(levelname)s - %(thread)d - %(filename)s:%(lineno)s - %(name)s - %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger = logging.getLogger("ctcloud")

    file_path = os.path.abspath(os.path.join(os.getenv("UPLOADDIR"), "demo.log"))
    file_handler = logging.FileHandler(file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger


def get_log_instance():
    if not get_log_instance.instance:
        get_log_instance.instance = init_logger()
    return get_log_instance.instance


get_log_instance.instance = None
