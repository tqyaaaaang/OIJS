#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.judge.judge


"""
module oijs.command.judge.judge
"""


import logging

from oijs.globals.log import log_decorator
from oijs.command.judge import temp_controller

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func
def judge(problem_dir, submission_dir):
    """
    judge
    """

    gl.info('judge with problem_dir = \'%s\', submission_dir = \'%s\'',
            problem_dir, submission_dir)

    ctl = temp_controller.start_controller()
    temp_controller.stop_controller(ctl)
