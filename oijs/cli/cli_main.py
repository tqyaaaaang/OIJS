#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli_main





import sys
import logging

from ..globals.config import global_conf
from . import cli
from .arguments import get_arguments





def cli_run ():
	logging.info ( 'OIJS started' )
	logging.debug ( 'configuration : ' + str ( global_conf.config ) )

	cur_argv = get_arguments.get_cli_main_arguments ()

	if cur_argv[0] != None:
		logging.info ( 'Detected arguments, run as run_by_argument mode' )
		cli.run_by_argument ( cur_argv )
	else:
		logging.info ( 'No arguments, run as cli mode' )
		cli.run_shell ()
