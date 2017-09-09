#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli





import sys

from .cli_ret_values import *
from . import command





def run_shell ():
	while 1:
		current_argv = input ( 'oijs>' ).split ()

		return_val = run_single_command ( current_argv )

		if return_val == RET_EXIT:
			break
		elif return_val == RET_FATAL:
			return return_val

	return RET_OK



def run_by_argument ():
	return_val = run_single_command ( sys.argv[1:] )

	if return_val == RET_EXIT:
		print ( 'ERROR : do not use command \'exit\' in single command mode.', file=sys.stderr )

	return return_val



def run_single_command ( argv ):
	return command.run_command ( argv )
