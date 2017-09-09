#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli_main





import sys

from . import cli





def cli_run ():
	if len ( sys.argv ) <= 1:
		cli.run_shell ()
	else:
		cli.run_by_argument ()
