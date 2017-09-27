#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli_complete





import sys
import os
import logging

from . import cli_complete_helper





def complete ( text, line, begidx, endidx ):
	return []



def complete_names ( text, line, begidx, endidx ):
	available_list = [
		'help',
		'exit',
		'init',
		'judge'
	]

	return cli_complete_helper.getprefix ( available_list, text )
