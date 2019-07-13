#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.help.show_help


"""
module oijs.command.help.show_help
"""


import logging

from oijs.globals.data import global_data
from oijs.cli.arguments import print_help
from oijs.globals.log import log_decorator

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func
def show_help():
    """
    show_help
    """

    if global_data.run_mode == 'cli':
        gl.debug('Detected cli mode')
        print_help.print_cli_help()
    elif global_data.run_mode == 'argv':
        gl.debug('Detected run_by_argument mode')
        print_help.print_cli_main_help()
