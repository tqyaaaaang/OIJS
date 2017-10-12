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
from ..globals.log import log_decorator

gl = logging.getLogger ( 'global' )





@log_decorator.log_func
def run_shell ():
	global_data.run_mode = 'cli'

	try:
		cli_cmd_class.cli_cmd ().cmdloop ()
	except exception.RET_FATAL_exception:
		gl.debug ( 'receiving return value RET_FATAL. Abort the cli' )
		return RET_FATAL
	except KeyboardInterrupt:
		gl.info ( 'receiving KeyboardInterrupt. Abort the cli' )
		print ()

	gl.debug ( 'exit normally' )

	return RET_OK



@log_decorator.log_func
def run_by_argument ():
	gl.info ( 'run_by_argument mode with arguments = \'{0}\''.format ( ' '.join ( sys.argv[1:] ) ) )

	global_data.run_mode = 'argv'

	global_arguments.current_arg = global_arguments.global_arg

	return_val = run_single_command ()

	if return_val == RET_EXIT:
		gl.warning ( 'using \'exit\' in run_by_argument mode' )
		print ( 'WARNING : do not use command \'exit\' in run_by_argument mode.', file=sys.stderr )

	return return_val



def run_single_command ():
	return command.run_command ()
