#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.init.create_dir





import logging
import os
import sys
import shutil
import yaml

from ...globals.log import log_decorator

gl = logging.getLogger ( 'global' )





class file_exist_exception ( Exception ):
	def __init__ ( self, filename ):
		self.filename = filename
	
	def error_msg ( self ):
		return 'ERROR : File \'{0}\' exists. Init failed. If you still want to init, use --force option'.format ( self.filename )





@log_decorator.log_func
def create_dir ( src, dst, config_filename, force = False ):
	gl.debug ( 'creating directory, source = \'{0}\', destination = \'{1}\', force = \'{2}\''.format ( src, dst, force ) )

	structure = {}
	with open ( config_filename ) as config_file:
		structure = yaml.load ( config_file )
	
	gl.debug ( 'load directory structure succeeded' )
	
	try:
		_create_dir_recursive ( src, dst, structure['root'], force )
	except file_exist_exception as e:
		gl.error ( e.error_msg () )
		print ( e.error_msg (), file=sys.stderr )





@log_decorator.log_func
def _create_dir_recursive ( src, dst, structure, force = False, cur_dir = '' ):
	if structure == 'EMPTY_DIR':
		return

	gl.debug ( 'creating directory in \'{0}\''.format ( cur_dir ) )
	for iterator in structure:
		if isinstance ( iterator, ( list, tuple, dict ) ):
			for val in iterator:
				cur_key = val
			element = cur_key
			target = os.path.join ( dst, element )
			if os.path.exists ( target ):
				if os.path.isfile ( target ):
					gl.debug ( '\'{0}\' is an existing file'.format ( os.path.join ( cur_dir, element ) ) )
					if not force:
						raise file_exist_exception ( os.path.join ( cur_dir, element ) )
					else:
						gl.debug ( 'Detected option force, remove the file' )
						os.remove ( target )
			if not os.path.exists ( target ):
				gl.debug ( 'Creating directory \'{0}\''.format ( os.path.join ( cur_dir, element ) ) )
				os.mkdir ( target )
			_create_dir_recursive ( os.path.join ( src, element ), os.path.join ( dst, element ), iterator[element], force, os.path.join ( cur_dir, element ) )
		else:
			element = iterator
			target = os.path.join ( dst, element )
			if os.path.exists ( target ):
				gl.debug ( '\'{0}\' exists'.format ( os.path.join ( cur_dir, element ) ) )
				if not force:
					raise file_exist_exception ( os.path.join ( cur_dir, element ) )
				else:
					gl.debug ( 'Detected option force, remove it' )
					if os.path.isfile ( target ):
						os.remove ( target )
					else:
						shutil.rmtree ( target )
			shutil.copy ( os.path.join ( src, element ), target )
			
			

