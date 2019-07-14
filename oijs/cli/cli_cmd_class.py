#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli_cmd_class


"""
module oijs.cli.cli_cmd_class
"""


import sys
import logging
import cmd

from oijs.cli.arguments import get_arguments
from oijs.globals.data import global_arguments
from oijs.cli import cli_ret_values
from oijs.cli import command
from oijs.globals.exceptions import exception
from oijs.cli import cli_complete

gl = logging.getLogger('global')   # pylint: disable=C0103


class cli_cmd(cmd.Cmd):   # pylint: disable=C0103
    """
    class cli_cmd
    """

    intro = 'Judge System for OI and ACM Command Line Interface'

    prompt = 'oijs> '

    def default(self, argv):   # pylint: disable=W0221
        """
        default
        """

        gl.debug('received one command : %s', argv)

        current_argv_list = argv.split()

        current_argv = get_arguments.get_cli_arguments(current_argv_list)

        gl.debug('command arguments : %s', current_argv)

        global_arguments.current_arg = current_argv

        return_val = command.run_command()

        if return_val == cli_ret_values.RET_EXIT:
            gl.info('receiving command \'exit\', exit normally')
            return True
        elif return_val == cli_ret_values.RET_FATAL:
            gl.debug('receiving fatal error, aborted the cli')
            raise exception.RET_FATAL_exception()

    def completedefault(self, text, line, begidx, endidx):   # pylint: disable=W0221
        """
        completedefault
        """

        return cli_complete.complete(text, line, begidx, endidx)

    def completenames(self, text, line, begidx, endidx):   # pylint: disable=W0221
        """
        completenames
        """

        return cli_complete.complete_names(text, line, begidx, endidx)

    # Special cases

    def emptyline(self):
        """
        emptyline
        """

        pass

    def do_help(self, argv):   # pylint: disable=W0221
        """
        do_help
        """

        return self.default('help {}'.format(argv))

    def do_EOF(self, argv):   # pylint: disable=W0613, R0201, W0221, C0103
        """
        do_EOF
        """

        gl.warning('received EOF. Ignored it')
        print()
        print('WARNING : Received EOF, ignored it. Use \'exit\' to exit',
              file=sys.stderr)
