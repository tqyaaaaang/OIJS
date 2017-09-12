#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli





import sys
import logging

from .cli_ret_values import *
from . import command
from ..globals.config import global_conf
from ..globals.data import global_arguments
from .arguments import get_arguments
from ..globals.data import global_data





def run_shell ():
	logging.debug ( 'function started' )

	global_data.run_mode = 'cli'

	while 1:
		current_argv_as_str = input ( 'oijs> ' )

		logging.debug ( 'received one command : {0}'.format ( current_argv_as_str ) )

		current_argv_list = current_argv_as_str.split ()

		current_argv = get_arguments.get_cli_arguments ( current_argv_list )

		logging.debug ( 'command arguments : {0}'.format ( str ( current_argv ) ) )

		return_val = run_single_command ( current_argv )

		if return_val == RET_EXIT:
			logging.info ( 'received command \'exit\', exit normally' )
			break
		elif return_val == RET_FATAL:
			logging.debug ( 'received fatal error, aborted the cli' )
			return return_val

	logging.debug ( 'exit normally' )

	return RET_OK



def run_by_argument ():
	logging.info ( 'function started' )
	logging.info ( 'run_by_argument mode with arguments = \'{0}\''.format ( ' '.join ( sys.argv[1:] ) ) )

	global_data.run_mode = 'argv'

	return_val = run_single_command ( global_arguments.global_arg )

	if return_val == RET_EXIT:
		logging.warning ( 'using \'exit\' in run_by_argument mode' )
		print ( 'WARNING : do not use command \'exit\' in run_by_argument mode.', file=sys.stderr )

	return return_val



def run_single_command ( argv ):
	return command.run_command ( argv )
