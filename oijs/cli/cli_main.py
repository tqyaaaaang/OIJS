#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli_main


"""
module oijs.cli.cli_main
"""


import logging

from ..globals.config import global_conf
from . import cli
from .arguments import get_arguments
from ..globals.data import global_arguments
from ..globals.log import log_decorator

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func
def cli_run():
    """
    cli_run
    """

    gl.info('OIJS started')
    gl.debug('configuration : %s', global_conf.config)

    get_arguments.get_cli_main_arguments()

    gl.debug('arguments : %s', global_arguments.global_arg)

    if global_arguments.global_arg.sub_command:
        gl.info('Detected arguments, run as run_by_argument mode')
        cli.run_by_argument()
    else:
        gl.info('No arguments, run as cli mode')
        cli.run_shell()
