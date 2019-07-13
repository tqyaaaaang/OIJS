#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.arguments.get_arguments


"""
module oijs.cli.arguments.get_arguments
"""


import sys
import logging
import argparse

from oijs.globals.data import global_arguments
from oijs.cli.arguments import init_helper
from oijs.globals.log import log_decorator

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func
def get_cli_main_arguments():
    """
    get_cli_main_arguments
    """

    arg_parser = argparse.ArgumentParser(
        prog='oijs',
        description='Judge System for OI and ACM',
        parents=[global_arg_parser, sub_command_arg_parser]
    )

    gl.debug('get parser completed')

    arg_val = arg_parser.parse_args(sys.argv[1:])

    global_arguments.global_arg = arg_val

    gl.info('load cli main arguments completed')


@log_decorator.log_func
def get_cli_arguments(argv):
    """
    get_cli_arguments
    """

    arg_parser = argparse.ArgumentParser(
        prog='oijs',
        description='Judge System for OI and ACM',
        usage='sub_command ...',
        parents=[sub_command_arg_parser],
        add_help=False
    )

    gl.debug('get parser completed')

    arg_val = None

    try:
        arg_val = arg_parser.parse_args(argv)
    except Exception:   # pylint: disable=W0703
        gl.error('received invalid command : \'{command}\'',
                 command=' '.join(argv))

    gl.debug('load cli commands completed')

    return arg_val


@log_decorator.log_func
def init_parsers():
    """
    init_parsers
    """

    global global_arg_parser   # pylint: disable=W0603, C0103
    global_arg_parser = init_helper.init_global_arg_parser()

    global sub_command_arg_parser   # pylint: disable=W0603, C0103
    sub_command_arg_parser = init_helper.init_sub_command_arg_parser()

    gl.info('init parsers succeeded')


global_arg_parser = None   # pylint: disable=C0103
sub_command_arg_parser = None   # pylint: disable=C0103
