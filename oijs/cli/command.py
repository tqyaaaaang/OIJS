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





def run_command ():
	logging.debug ( 'function started' )

	argv = global_arguments.current_arg

	logging.info ( 'running command : {0}'.format ( str ( argv ) ) )

	print ( 'Running command : {0}'.format ( str ( argv ) ) )

	if ( argv == None ) or ( argv.sub_command == None ):
		logging.debug ( 'running command : received empty command' )
		return RET_EMPTY
	elif argv.sub_command == 'exit':
		logging.debug ( 'received exit' )
		return RET_EXIT
	elif argv.sub_command in available_commands:
		logging.debug ( 'running command : {0}'.format ( argv.sub_command ) )
		available_commands[argv.sub_command] ()

	return RET_OK





available_commands = {
	'help': show_help.show_help,
	'init': init.init
}
