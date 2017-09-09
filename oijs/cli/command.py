#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.command





import sys

from .cli_ret_values import *





def run_command ( argv ):
	arg_str = ''
	for val in argv: arg_str += val + ' '
	print ( "Running command : " + arg_str )

	if argv == [ 'exit' ]:
		return RET_EXIT

	return RET_OK
