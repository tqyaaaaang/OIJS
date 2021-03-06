#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: globals.config.conf_helper





import yaml
import sys
import os
import shutil
from ..data import global_data
from ..exception.exception import oijs_exception





def load_conf ( filename ):
	config = {}
	with open ( filename ) as curfile:
		config = yaml.load ( curfile )
	return config



def join_conf ( default_conf, custom_conf, current_config = '' ):
	if ( isinstance ( default_conf, dict ) ) and ( not isinstance ( custom_conf, dict ) ):
		if custom_conf == None: return default_conf
		raise oijs_exception ( 'FATAL ERROR : {0} should be a map. An item was found.'.format ( current_config ) )

	cur_conf = default_conf

	for cur in custom_conf:
		if cur in cur_conf:
			if ( isinstance ( cur_conf[cur], dict ) ):
				join_conf ( cur_conf[cur], custom_conf[cur], current_config + '.' + cur )
			else:
				if ( isinstance ( custom_conf[cur], dict ) ):
					raise oijs_exception ( 'FATAL ERROR : configuration {0}.{1} should be an item. A map was found.'.format ( current_config, cur ) )

				if ( isinstance ( cur_conf[cur], list ) ):
					if ( isinstance ( custom_conf[cur], list ) ):
						cur_conf[cur] = custom_conf[cur]
					else:
						cur_conf[cur] = [ custom_conf[cur] ]
				else:
					if ( isinstance ( custom_conf[cur], list ) ):
						if len ( custom_conf[cur] ) == 1:
							cur_conf[cur] = custom_conf[cur][0]
						else:
							raise oijs_exception ( 'FATAL ERROR : configuration {0}.{1} should be an item. A list was found.'.format ( current_config, cur ) )
					else:
						cur_conf[cur] = custom_conf[cur]
		else:
			raise oijs_exception ( 'FATAL ERROR : configuration {0}.{1} does not exist.'.format ( current_config, cur ) )

	return cur_conf



def check_conf_exist ():
	if not os.path.exists ( os.path.expanduser ( '~/.oijs' ) ):
		print ( 'Can\'t find config directory. Generating one.' )

		shutil.copytree ( global_data.current_dir + '/lib/oijs/oijs_dir', os.path.expanduser ( '~/.oijs' ) )
