#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: global.log.log_config





import logging
import os
from ..config import global_conf





def config_log ():
	logging.basicConfig (
		format = '%(asctime)s : %(filename)s ( %(funcName)s ) : %(levelname)s : %(message)s',
		datefmt = '%Y-%m-%d %H:%M:%S',
		filename = os.path.expanduser ( global_conf.config['log']['file'] ),
		filemode = global_conf.config['log']['mode'],
		level = global_conf.config['log']['level']
	)
