#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.arguments.init_helper





import sys
import argparse
import logging

from ...globals.log import log_decorator

gl = logging.getLogger ( 'global' )





@log_decorator.log_func
def init_global_arg_parser ():
	arg_parser = argparse.ArgumentParser (
		add_help = False
	)

	gl.debug ( 'created parser' )

	arg_parser.add_argument (
		'-d', '--directory',
		default = '.',
		help = 'specify the directory of the project'
	)

	gl.debug ( 'added argument --directory' )

	return arg_parser




@log_decorator.log_func
def init_sub_command_arg_parser ():
	arg_parse = argparse.ArgumentParser (
		add_help = False
	)

	gl.debug ( 'created parser' )

	sub_arg = arg_parse.add_subparsers (
		title = 'sub commands',
		dest = 'sub_command',
		metavar = 'sub_command'
	)

	gl.debug ( 'added subparser sub_arg' )

	init_exit ( sub_arg )
	init_help ( sub_arg )
	init_init ( sub_arg )
	init_judge ( sub_arg )

	gl.debug ( 'success' )

	return arg_parse



@log_decorator.log_func
def init_exit ( sub_arg ):
	cur_parser = sub_arg.add_parser ( 'exit', help = 'exit OIJS' )
	gl.debug ( 'added sub_command exit' )



@log_decorator.log_func
def init_help ( sub_arg ):
	cur_parser = sub_arg.add_parser ( 'help', help = 'show this help message' )
	gl.debug ( 'added sub_command help' )



@log_decorator.log_func
def init_init ( sub_arg ):
	cur_parser = sub_arg.add_parser ( 'init', help = 'Create a new project' )
	cur_parser.add_argument ( 'init_type', help = 'The type of the project', choices = [ 'problem' ] )
	cur_parser.add_argument ( '-f', '--force', help = 'Overwrite existing files', action = 'store_true' )
	gl.debug ( 'added sub_command init' )



@log_decorator.log_func
def init_judge ( sub_arg ):
	cur_parser = sub_arg.add_parser ( 'judge', help = 'Judge a solution' )
	cur_parser.add_argument ( 'submission_id', help = 'The id of the submission' )
	gl.debug ( 'added sub_command judge' )
