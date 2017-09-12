#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.arguments.print_help





import sys
import logging
import argparse

from ...globals.data import global_arguments
from . import init_helper
from . import get_arguments





def print_cli_main_help ():
	logging.debug ( 'started' )

	arg_parser = argparse.ArgumentParser (
		prog = 'oijs',
		description = 'Judge System for OI and ACM',
		parents = [ get_arguments.global_arg_parser, get_arguments.sub_command_arg_parser ]
	)

	logging.debug ( 'get parser completed' )

	arg_parser.print_help ()




def print_cli_help ():
	logging.debug ( 'started' )

	arg_parser = argparse.ArgumentParser (
		prog = 'oijs',
		description = 'Judge System for OI and ACM',
		usage = 'sub_command ...',
		parents = [ get_arguments.sub_command_arg_parser ],
		add_help = False
	)

	logging.debug ( 'get parser completed' )

	arg_parser.print_help ()
