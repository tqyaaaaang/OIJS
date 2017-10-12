#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: global.log.log_decorator





import logging
import os
import sys
from functools import wraps
from ..exception import exception
import time
import inspect
from ..config import global_conf
import wrapt
import functools
import copy





class _log_func_tmp_handler:
	def __init__ ( self, func, logger = logging.getLogger () ):
		self.logger = logger
		self.funcname = func.__name__
		self.filename = os.path.basename ( inspect.getfile ( func ) )
	
	def __enter__ ( self ):
		self.old_handlers = self.logger.handlers
		self.logger.handlers = []
		self.new_handlers = []

		for handler in self.old_handlers:
			self.logger.removeHandler ( handler )

		for old_handler in self.old_handlers:
			new_handler = copy.copy ( old_handler )

			fmt = old_handler.formatter._fmt
			fmt = fmt.replace ( '%(filename)s', self.filename )
			fmt = fmt.replace ( '%(funcName)s', self.funcname )

			new_handler.setFormatter (
				logging.Formatter (
					fmt = fmt,
					datefmt = '%Y-%m-%d %H:%M:%S'
				)
			)

			self.new_handlers.append ( new_handler )
			self.logger.addHandler ( new_handler )
	
	def __exit__ ( self, *ignore ):
		for handler in self.new_handlers:
			self.logger.removeHandler ( handler )
		
		for handler in self.old_handlers:
			self.logger.addHandler ( handler )





def log_func ( func = None, logger = 'global' ):
	if func is None:
		return functools.partial ( log_func, logger = logger )

	@ wrapt.decorator
	def wrapper ( func, instance, args, kwargs ):
		start_msg = 'started'

		if logger and not logger in logging.Logger.manager.loggerDict:
			raise exception.oijs_exception ( 'logger is not a valid LoggerClass in decorator log_func' )

		cur_logger = logging.getLogger ( logger )

		with _log_func_tmp_handler ( func, cur_logger ):
			cur_logger.debug ( start_msg )
		
		start_time = time.time ()

		try:
			return_val = func ( *args, **kwargs )
		except:
			except_msg = 'received exception, exit the function'

			with _log_func_tmp_handler ( func, cur_logger ):
				cur_logger.debug ( except_msg )
			
			raise

		stop_time = time.time ()

		used_time = ( stop_time - start_time ) * 1000

		exit_msg = 'exit normally, time used : {0:.3f} ms'.format ( used_time )

		with _log_func_tmp_handler ( func, cur_logger ):
			cur_logger.debug ( exit_msg )
		
		return return_val
	
	return wrapper ( func )