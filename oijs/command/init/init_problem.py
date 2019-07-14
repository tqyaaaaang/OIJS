#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.init.init_problem


"""
module oijs.command.init.init_problem
"""


import logging
import os

from oijs.globals.data import global_arguments
from oijs.globals.data import global_data
from oijs.globals.log import log_decorator
from oijs.command.init import create_dir

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func
def init_problem():
    """
    init_problem
    """

    print('Type: problem')

    create_dir.create_dir(
        'oijs.misc.init_dir.problem_dir',
        global_arguments.global_arg.directory,
        'oijs.command.init.dir_structure',
        'problem_dir.yml',
        global_arguments.current_arg.force
    )
