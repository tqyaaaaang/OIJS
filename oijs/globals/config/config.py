#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: global.config.global_conf





from . import global_conf
from . import log_config
from . import conf_helper





def load_conf ():
	before_load_conf ()
	main_load_conf ()
	after_load_conf ()



def before_load_conf ():
	conf_helper.check_conf_exist ()



def main_load_conf ():
	global_conf.load_conf ()



def after_load_conf ():
	log_config.config_log ()
