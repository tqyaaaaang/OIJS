#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.command





import sys
import logging

from .cli_ret_values import *
from .commands import show_help
from .commands import init
from ..globals.data import global_arguments
from ..globals.log import log_decorator

gl = logging.getLogger ( 'global' )





@log_decorator.log_func
def run_command ():
	argv = global_arguments.current_arg

	gl.info ( 'running command : {0}'.format ( str ( argv ) ) )

	print ( 'Running command : {0}'.format ( str ( argv ) ) )

	if ( argv == None ) or ( argv.sub_command == None ):
		gl.debug ( 'running command : received empty command' )
		return RET_EMPTY
	elif argv.sub_command == 'exit':
		gl.debug ( 'received exit' )
		return RET_EXIT
	elif argv.sub_command in available_commands:
		gl.debug ( 'running command : {0}'.format ( argv.sub_command ) )
		available_commands[argv.sub_command] ()

	return RET_OK





available_commands = {
	'help': show_help.show_help,
	'init': init.init
}
