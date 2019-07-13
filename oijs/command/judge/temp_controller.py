#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.judge.temp_controller


"""
module oijs.command.judge.temp_controller
"""


import logging
import multiprocessing

from oijs.globals.log import log_decorator

from oijs.controller import controller

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func
def start_controller():
    """
    start_controller
    """

    ctl = multiprocessing.Process(
        target=controller.main
    )

    ctl.start()

    return ctl


@log_decorator.log_func
def stop_controller(ctl):
    """
    stop_controller
    """

    ctl.join(timeout=0.1)

    if ctl.is_alive():
        kill_controller(ctl)


@log_decorator.log_func
def kill_controller(ctl):
    """
    kill_controller
    """

    ctl.terminate()
