#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.init.init_problem


"""
module oijs.command.init.init_problem
"""


import logging
import os

from ...globals.data import global_arguments
from ...globals.data import global_data
from ...globals.log import log_decorator
from . import create_dir

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func
def init_problem():
    """
    init_problem
    """

    print('Type: problem')

    create_dir.create_dir(
        os.path.join(global_data.current_dir, 'lib/oijs/init_dir/problem_dir'),
        global_arguments.global_arg.directory,
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     'dir_structure/problem_dir.yml'),
        global_arguments.current_arg.force
    )
