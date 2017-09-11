#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli





import sys
import logging

from .cli_ret_values import *
from . import command
from ..globals.config import global_conf





def run_shell ():
	logging.debug ( 'function started' )

	while 1:
		current_argv_as_str = input ( 'oijs> ' )

		logging.debug ( 'received one command : {0}'.format ( current_argv_as_str ) )

		current_argv = current_argv_as_str.split ()

		return_val = run_single_command ( current_argv )

		if return_val == RET_EXIT:
			logging.info ( 'received command \'exit\', exit normally' )
			break
		elif return_val == RET_FATAL:
			logging.debug ( 'received fatal error, aborted the cli' )
			return return_val

	logging.debug ( 'exit normally' )

	return RET_OK



def run_by_argument ( argv ):
	logging.info ( 'function started' )
	argv_str = ''
	for val in sys.argv[1:]: argv_str += str ( val ) + ' '
	logging.info ( 'run_by_argument mode with arguments = \'{0}\''.format ( argv_str[:-1] ) )

	return_val = run_single_command ( argv )

	if return_val == RET_EXIT:
		logging.warning ( 'using \'exit\' in run_by_argument mode' )
		print ( 'WARNING : do not use command \'exit\' in run_by_argument mode.', file=sys.stderr )

	return return_val



def run_single_command ( argv ):
	return command.run_command ( argv )
