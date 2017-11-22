#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: globals.log.log_config


"""
module oijs.globals.log.log_config
"""


import logging
import os
from ..config import global_conf


def config_log():
    """
    config_log
    """

    global_logger = logging.getLogger('global')
    global_logger_handlers = logging.FileHandler(
        filename=os.path.expanduser(global_conf.config['log']['file']),
        mode=global_conf.config['log']['mode']
    )
    global_logger_handlers.setFormatter(
        logging.Formatter(
            fmt='{asctime} : {filename} ( {funcName} ) : {levelname} : {message}',
            datefmt='%Y-%m-%d %H:%M:%S',
            style='{'
        )
    )
    global_logger.addHandler(global_logger_handlers)
    global_logger.setLevel(global_conf.config['log']['level'])
