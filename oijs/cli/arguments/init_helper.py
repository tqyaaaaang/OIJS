#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.arguments.init_helper





import sys
import argparse
import logging

gl = logging.getLogger ( 'global' )





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

	gl.debug ( 'success' )

	return arg_parse



def init_exit ( sub_arg ):
	cur_parser = sub_arg.add_parser ( 'exit', help = 'exit OIJS' )
	gl.debug ( 'added sub_command exit' )



def init_help ( sub_arg ):
	cur_parser = sub_arg.add_parser ( 'help', help = 'show this help message' )
	gl.debug ( 'added sub_command help' )



def init_init ( sub_arg ):
	cur_parser = sub_arg.add_parser ( 'init', help = 'Create a new project' )
	cur_parser.add_argument ( 'init_type', help = 'The type of the project', choices = [ 'problem' ] )
	gl.debug ( 'added sub_command init' )
