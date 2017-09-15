#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: globals.exception.exception





class oijs_exception ( Exception ):
	def __init__ ( self, error_content ):
		self._error = error_content



	def error ( self ):
		return self._error





class RET_FATAL_exception ( Exception ):
	pass
