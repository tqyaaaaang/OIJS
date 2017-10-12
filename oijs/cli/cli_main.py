#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli_main





import sys
import logging

from ..globals.config import global_conf
from . import cli
from .arguments import get_arguments
from ..globals.data import global_arguments
from ..globals.log import log_decorator

gl = logging.getLogger ( 'global' )





@log_decorator.log_func
def cli_run ():
	gl.info ( 'OIJS started' )
	gl.debug ( 'configuration : ' + str ( global_conf.config ) )

	get_arguments.get_cli_main_arguments ()

	gl.debug ( 'arguments : ' + str ( global_arguments.global_arg ) )

	if global_arguments.global_arg.sub_command:
		gl.info ( 'Detected arguments, run as run_by_argument mode' )
		cli.run_by_argument ()
	else:
		gl.info ( 'No arguments, run as cli mode' )
		cli.run_shell ()
