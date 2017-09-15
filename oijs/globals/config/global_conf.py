#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: global.config.global_conf





from . import conf_helper
import sys
import os
from ..exception.exception import oijs_exception





config = {}

def load_conf ():
	default_conf = conf_helper.load_conf ( os.path.dirname ( os.path.abspath ( __file__ ) ) + '/default_conf/oijs_global_conf.yml' )
	custom_conf = conf_helper.load_conf ( os.path.expanduser ( '~/.oijs/config.yml' ) )
	global config
	try:
		config = conf_helper.join_conf ( default_conf, custom_conf )
	except oijs_exception as err:
		print ( err.error (), file=sys.stderr )
		exit ( 1 )
