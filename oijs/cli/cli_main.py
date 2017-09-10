#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli_main





import sys
import logging
from ..globals.config import global_conf

from . import cli





def cli_run ():
	logging.info ( 'OIJS started' )
	logging.debug ( 'configuration : ' + str ( global_conf.config ) )
	if len ( sys.argv ) <= 1:
		logging.info ( 'No argument, run as cli mode' )
		cli.run_shell ()
	else:
		logging.info ( 'Detected arguments, run as run_by_argument mode' )
		cli.run_by_argument ()
