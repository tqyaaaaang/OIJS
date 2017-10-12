#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.help.show_help





import logging

from ...globals.data import global_data
from ...cli.arguments import print_help

gl = logging.getLogger ( 'global' )





def show_help ():
	gl.debug ( 'started' )
	if global_data.run_mode == 'cli':
		gl.debug ( 'Detected cli mode' )
		print_help.print_cli_help ()
	elif global_data.run_mode == 'argv':
		gl.debug ( 'Detected run_by_argument mode' )
		print_help.print_cli_main_help ()
