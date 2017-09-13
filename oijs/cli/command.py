#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.command





import sys
import logging

from .cli_ret_values import *
from ..command.help import show_help





def run_command ( argv ):
	logging.debug ( 'function started' )

	logging.info ( 'running command : {0}'.format ( str ( argv ) ) )

	print ( 'Running command : {0}'.format ( str ( argv ) ) )

	if ( argv == None ) or ( argv.sub_command == None ):
		logging.debug ( 'running command : received empty command' )
		return RET_EMPTY
	elif argv.sub_command == 'exit':
		logging.debug ( 'received exit' )
		return RET_EXIT
	elif argv.sub_command == 'help':
		logging.debug ( 'running command : help' )
		show_help.show_help ()

	return RET_OK
