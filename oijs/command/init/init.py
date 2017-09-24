#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.init.init





import logging
from ...globals.data import global_arguments
from . import init_problem





def init ():
	logging.debug ( 'started' )
	logging.info ( 'init type: {0}'.format ( global_arguments.current_arg.init_type ) )
	print ( 'initializing...' )
	available_types[global_arguments.current_arg.init_type] ()





available_types = {
	'problem': init_problem.init_problem
}
