#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.init.init


"""
module oijs.command.init.init
"""


import logging
from oijs.globals.data import global_arguments
from oijs.command.init import init_problem
from oijs.globals.log import log_decorator

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func
def init():
    """
    init
    """

    gl.info('init type: %s', global_arguments.current_arg.init_type)
    print('Initializing...')
    available_types[global_arguments.current_arg.init_type]()


available_types = {   # pylint: disable=C0103
    'problem': init_problem.init_problem
}
