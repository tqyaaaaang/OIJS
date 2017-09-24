#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: globals.data.global_data





import sys
import os





def load_data ():
	global current_dir
	current_dir = os.path.abspath ( '{0}/..'.format ( sys.path[0] ) )





current_dir = ''

run_mode = None
