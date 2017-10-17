#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.judge.judge





import sys
import os
import logging

from ...globals.data import global_arguments
from ...globals.log import log_decorator
from . import temp_controller

gl = logging.getLogger ( 'global' )





@log_decorator.log_func
def judge ( problem_dir, submission_dir ):
	gl.info ( 'judge with problem_dir = \'{0}\', submission_dir = \'{1}\''.format ( problem_dir, submission_dir ) )

	ctl = temp_controller.start_controller ()
	temp_controller.stop_controller ( ctl )
