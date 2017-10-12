#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.init.init_problem





import logging
import os
import shutil
from ...globals.data import global_arguments
from ...globals.data import global_data
from ...globals.log import log_decorator

gl = logging.getLogger ( 'global' )





@log_decorator.log_func
def init_problem ():
	print ( 'Type: problem' )

	os.system ( 'cp -r {0} {1}'.format ( global_data.current_dir + '/lib/oijs/init_dir/problem_dir/*', global_arguments.global_arg.directory ) )
