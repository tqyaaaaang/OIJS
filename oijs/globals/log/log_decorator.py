#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: globals.log.log_decorator


"""
module oijs.globals.log.log_decorator
"""


import logging
import os
import time
import inspect
import functools
import copy
import wrapt
from oijs.globals.exception import exception


class _log_func_tmp_handler:   # pylint: disable=R0903, C0103
    """
    class _log_func_tmp_handler
    """

    def __init__(self, func, logger=logging.getLogger()):
        """
        __init__
        """

        self.logger = logger
        self.funcname = func.__name__
        self.filename = os.path.basename(inspect.getfile(func))
        self.old_handlers = None
        self.new_handlers = None

    def __enter__(self):
        """
        __enter__
        """

        self.old_handlers = self.logger.handlers
        self.logger.handlers = []
        self.new_handlers = []

        for handler in self.old_handlers:
            self.logger.removeHandler(handler)

        for old_handler in self.old_handlers:
            new_handler = copy.copy(old_handler)

            fmt = old_handler.formatter._fmt   # pylint: disable=W0212
            fmt = fmt.replace('{filename}', self.filename)
            fmt = fmt.replace('{funcName}', self.funcname)

            new_handler.setFormatter(
                logging.Formatter(
                    fmt=fmt,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    style='{'
                )
            )

            self.new_handlers.append(new_handler)
            self.logger.addHandler(new_handler)

    def __exit__(self, *ignore):
        """
        __exit__
        """

        for handler in self.new_handlers:
            self.logger.removeHandler(handler)

        for handler in self.old_handlers:
            self.logger.addHandler(handler)


def log_func(func=None, logger='global', logger_may_not_exist=False):
    """
    log_func
    """

    if func is None:
        return functools.partial(log_func, logger=logger, logger_may_not_exist=logger_may_not_exist)

    @ wrapt.decorator
    def wrapper(func, instance, args, kwargs):   # pylint: disable=W0613
        """
        wrapper
        """

        start_msg = 'started'

        if logger and logger not in logging.Logger.manager.loggerDict:
            if logger_may_not_exist:
                return func(*args, **kwargs)
            else:
                raise exception.oijs_exception(
                    'logger is not a valid LoggerClass in decorator log_func')

        cur_logger = logging.getLogger(logger)

        with _log_func_tmp_handler(func, cur_logger):
            cur_logger.debug(start_msg)

        start_time = time.time()

        try:
            return_val = func(*args, **kwargs)
        except:
            except_msg = 'received exception, exit the function'

            with _log_func_tmp_handler(func, cur_logger):
                cur_logger.debug(except_msg)

            raise

        stop_time = time.time()

        used_time = (stop_time - start_time) * 1000

        exit_msg = 'exit normally, time used : {0:.3f} ms'.format(used_time)

        with _log_func_tmp_handler(func, cur_logger):
            cur_logger.debug(exit_msg)

        return return_val

    return wrapper(func)   # pylint: disable=E1120
