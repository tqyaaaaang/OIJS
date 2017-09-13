#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli_cmd_class





import sys
import logging
import cmd
import logging

from . import command
from .arguments import get_arguments
from ..globals.data import global_arguments
from .cli_ret_values import *
from . import cli
from ..globals.exception import exception
from . import cli_complete





class cli_cmd ( cmd.Cmd ):
	intro = 'Judge System for OI and ACM Command Line Interface'

	prompt = 'oijs> '



	def default ( self, argv ):
		logging.debug ( 'received one command : {0}'.format ( argv ) )

		current_argv_list = argv.split ()

		current_argv = get_arguments.get_cli_arguments ( current_argv_list )

		logging.debug ( 'command arguments : {0}'.format ( str ( current_argv ) ) )

		global_arguments.current_arg = current_argv

		return_val = cli.run_single_command ()

		if return_val == RET_EXIT:
			logging.info ( 'received command \'exit\', exit normally' )
			return True
		elif return_val == RET_FATAL:
			logging.debug ( 'received fatal error, aborted the cli' )
			raise exception.RET_FATAL_exception ()



	def completedefault ( self, text, line, begidx, endidx ):
		return cli_complete.complete ( text, line, begidx, endidx )

	def completenames (  self, text, line, begidx, endidx ):
		return self.completedefault ( text, line, begidx, endidx )



	# Special cases

	def emptyline ( self ):
		pass

	def do_help ( self, argv ):
		return self.default ( 'help {0}'.format ( argv ) )

	def do_EOF ( self, argv ):
		logging.warning ( 'received EOF. Ignored it' )
		print ()
		print ( 'WARNING : Received EOF, ignored it. Use \'exit\' to exit', file=sys.stderr )
