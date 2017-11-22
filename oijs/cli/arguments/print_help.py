#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.arguments.print_help


"""
module ijs.cli.arguments.print_help
"""


import logging
import argparse

from . import get_arguments
from ...globals.log import log_decorator

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func
def print_cli_main_help():
    """
    print_cli_main_help
    """

    arg_parser = argparse.ArgumentParser(
        prog='oijs',
        description='Judge System for OI and ACM',
        parents=[get_arguments.global_arg_parser,
                 get_arguments.sub_command_arg_parser]
    )

    gl.debug('get parser completed')

    arg_parser.print_help()


@log_decorator.log_func
def print_cli_help():
    """
    print_cli_help
    """

    arg_parser = argparse.ArgumentParser(
        prog='oijs',
        description='Judge System for OI and ACM',
        usage='sub_command ...',
        parents=[get_arguments.sub_command_arg_parser],
        add_help=False
    )

    gl.debug('get parser completed')

    arg_parser.print_help()
