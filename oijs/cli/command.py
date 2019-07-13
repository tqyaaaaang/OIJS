#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.command


"""
module oijs.cli.command
"""


import logging

from oijs.cli import cli_ret_values
from oijs.cli.commands import show_help
from oijs.cli.commands import init
from oijs.cli.commands import judge
from oijs.globals.data import global_arguments
from oijs.globals.log import log_decorator

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func
def run_command():
    """
    run_commmand
    """

    argv = global_arguments.current_arg

    gl.info('running command : %s', argv)

    print('Running command : ', argv)

    if (argv is None) or (argv.sub_command is None):
        gl.debug('running command : received empty command')
        return cli_ret_values.RET_EMPTY
    elif argv.sub_command == 'exit':
        gl.debug('received exit')
        return cli_ret_values.RET_EXIT
    elif argv.sub_command in available_commands:
        gl.debug('running command : %s', argv.sub_command)
        available_commands[argv.sub_command]()

    return cli_ret_values.RET_OK


available_commands = {   # pylint: disable=C0103
    'help': show_help.show_help,
    'init': init.init,
    'judge': judge.judge
}
