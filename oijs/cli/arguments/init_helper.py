#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.arguments.init_helper





import sys
import argparse
import logging





def init_global_arg_parser ():
	logging.debug ( 'started' )

	arg_parser = argparse.ArgumentParser (
		add_help = False
	)

	logging.debug ( 'created parser' )

	arg_parser.add_argument (
		'-d', '--directory',
		default = '.',
		help = 'specify the directory of the project'
	)

	logging.debug ( 'added argument --directory' )

	return arg_parser




def init_sub_command_arg_parser ():
	logging.debug ( 'started' )

	arg_parse = argparse.ArgumentParser (
		add_help = False
	)

	logging.debug ( 'created parser' )

	sub_arg = arg_parse.add_subparsers (
		title = 'sub commands',
		dest = 'sub_command',
		metavar = 'sub_command'
	)

	logging.debug ( 'added subparser sub_arg' )

	init_exit ( sub_arg )
	init_help ( sub_arg )
	init_init ( sub_arg )

	logging.debug ( 'success' )

	return arg_parse



def init_exit ( sub_arg ):
	logging.debug ( 'started' )
	cur_parser = sub_arg.add_parser ( 'exit', help = 'exit OIJS' )
	logging.debug ( 'added sub_command exit' )



def init_help ( sub_arg ):
	logging.debug ( 'started' )
	cur_parser = sub_arg.add_parser ( 'help', help = 'show this help message' )
	logging.debug ( 'added sub_command help' )



def init_init ( sub_arg ):
	logging.debug ( 'started' )
	cur_parser = sub_arg.add_parser ( 'init', help = 'Create a new project' )
	cur_parser.add_argument ( 'init_type', help = 'The type of the project', choices = [ 'problem' ] )
	logging.debug ( 'added sub_command init' )
