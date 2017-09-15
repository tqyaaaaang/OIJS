#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.arguments.get_arguments





import sys
import logging
import argparse

from ...globals.data import global_arguments
from . import init_helper





def get_cli_main_arguments ():
	logging.debug ( 'started' )

	arg_parser = argparse.ArgumentParser (
		prog = 'oijs',
		description = 'Judge System for OI and ACM',
		parents = [ global_arg_parser, sub_command_arg_parser ]
	)

	logging.debug ( 'get parser completed' )

	arg_val = arg_parser.parse_args ( sys.argv[1:] )

	global_arguments.global_arg = arg_val

	logging.info ( 'load cli main arguments completed' )



def get_cli_arguments ( argv ):
	logging.debug ( 'started' )

	arg_parser = argparse.ArgumentParser (
		prog = 'oijs',
		description = 'Judge System for OI and ACM',
		usage = 'sub_command ...',
		parents = [ sub_command_arg_parser ],
		add_help = False
	)

	logging.debug ( 'get parser completed' )

	arg_val = None

	try:
		arg_val = arg_parser.parse_args ( argv )
	except :
		logging.error ( 'received invalid command : \'{0}\''.format ( ' '.join ( argv ) ) )

	logging.debug ( 'load cli commands completed' )

	return arg_val



def init_parsers ():
	logging.debug ( 'started' )

	global global_arg_parser
	global_arg_parser = init_helper.init_global_arg_parser ()

	global sub_command_arg_parser
	sub_command_arg_parser = init_helper.init_sub_command_arg_parser ()

	logging.info ( 'init parsers succeeded' )





global_arg_parser = None
sub_command_arg_parser = None
