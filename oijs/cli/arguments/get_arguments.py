#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.arguments.get_arguments





import sys
import argparse

from ...globals.data import global_arguments





def get_cli_main_arguments ():
	arg_parser = argparse.ArgumentParser (
		prog = 'oijs',
		description = 'Judge System for OI and ACM'
	)

	arg_parser.add_argument (
		'-d', '--directory',
		default = '.',
		help = 'specify the directory of the project'
	)

	arg_parser.add_argument (
		'sub_command',
		choices = [ 'exit' ],
		help = 'sub command. Leave it empty if you want to enter cli mode.',
		metavar = 'sub_command',
		nargs = '?'
	)

	arg_parser.add_argument (
		'sub_command_options',
		nargs = argparse.REMAINDER,
		metavar = ''
	)

	arg_val = arg_parser.parse_args ( sys.argv[1:] )

	global_arguments.directory = arg_val.directory

	return [ arg_val.sub_command ] + arg_val.sub_command_options
