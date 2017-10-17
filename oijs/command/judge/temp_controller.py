#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.judge.temp_controller





import sys
import os
import logging
import multiprocessing

from ...globals.data import global_arguments
from ...globals.log import log_decorator

from ...controller import controller

gl = logging.getLogger ( 'global' )





@log_decorator.log_func
def start_controller ():
	ctl = multiprocessing.Process (
		target = controller.main
	)

	ctl.start ()

	return ctl



@log_decorator.log_func
def stop_controller ( ctl ):
	ctl.join ( timeout = 0.1 )

	if ctl.is_alive ():
		kill_controller ( ctl )



@log_decorator.log_func
def kill_controller ( ctl ):
	ctl.terminate ()
