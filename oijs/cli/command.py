#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.command





import sys
import logging

from .cli_ret_values import *





def run_command ( argv ):
	logging.debug ( 'function started' )

	argv_str = ''
	for val in argv: argv_str += str ( val ) + ' '
	logging.info ( 'running command : {0}'.format ( argv_str ) )

	print ( 'Running command : {0}'.format ( argv_str ) )

	if argv == [ 'exit' ]:
		return RET_EXIT

	return RET_OK
