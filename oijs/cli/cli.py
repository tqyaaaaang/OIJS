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
from . import cli_cmd_class
from ..globals.exception import exception





def run_shell ():
	logging.debug ( 'function started' )

	global_data.run_mode = 'cli'

	try:
		cli_cmd_class.cli_cmd ().cmdloop ()
	except exception.RET_FATAL_exception:
		logging.debug ( 'receiving return value RET_FATAL. Aborted the cli' )
		return RET_FATAL

	logging.debug ( 'exit normally' )

	return RET_OK



def run_by_argument ():
	logging.info ( 'function started' )
	logging.info ( 'run_by_argument mode with arguments = \'{0}\''.format ( ' '.join ( sys.argv[1:] ) ) )

	global_data.run_mode = 'argv'

	global_arguments.current_arg = global_arguments.global_arg

	return_val = run_single_command ()

	if return_val == RET_EXIT:
		logging.warning ( 'using \'exit\' in run_by_argument mode' )
		print ( 'WARNING : do not use command \'exit\' in run_by_argument mode.', file=sys.stderr )

	return return_val



def run_single_command ():
	return command.run_command ()
