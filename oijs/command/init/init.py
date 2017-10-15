#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.init.init





import logging
from ...globals.data import global_arguments
from . import init_problem
from ...globals.log import log_decorator

gl = logging.getLogger ( 'global' )





@log_decorator.log_func
def init ():
	gl.info ( 'init type: {0}'.format ( global_arguments.current_arg.init_type ) )
	print ( 'Initializing...' )
	available_types[global_arguments.current_arg.init_type] ()





available_types = {
	'problem': init_problem.init_problem
}
