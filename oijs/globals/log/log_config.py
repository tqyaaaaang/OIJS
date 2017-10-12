#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: global.log.log_config





import logging
import os
from ..config import global_conf





def config_log ():
	global_logger = logging.getLogger ( 'global' )
	global_logger_handlers = logging.FileHandler (
		filename = os.path.expanduser ( global_conf.config['log']['file'] ),
		mode = global_conf.config['log']['mode']
	)
	global_logger_handlers.setFormatter (
		logging.Formatter (
			fmt = '%(asctime)s : %(filename)s ( %(funcName)s ) : %(levelname)s : %(message)s',
			datefmt = '%Y-%m-%d %H:%M:%S'
		)
	)
	global_logger.addHandler ( global_logger_handlers )
	global_logger.setLevel ( global_conf.config['log']['level'] )
