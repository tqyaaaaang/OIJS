#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: setup.py

from setuptools import setup, find_packages
import os

with open ( 'README.md', encoding='utf-8' ) as readme_file:
	long_description = readme_file.read ()



def get_all_files ( src, dst ):
	cur_files = os.listdir ( src )
	in_src = []
	cur_data_files = []
	for element in cur_files:
		if os.path.isfile ( src + element ):
			in_src.append ( src + element )
		else:
			cur_data_files.extend ( get_all_files ( src + element + '/', dst + element + '/' ) )
	if in_src:
		cur_data_files.append ( ( dst, in_src ) )
	return cur_data_files


data_files = get_all_files ( 'lib/', 'lib/oijs/' ) + get_all_files ( 'docs/', 'share/doc/oijs/' )



setup (
	name = 'oijs',
	version = '1.1.0',

	description = 'Judge System for OI and ACM',
	long_description = long_description,

	author = 'tqyaaaaang',
	author_email = 'tqyangoi1@gmail.com',

	keywords = 'oi judge',

	packages = find_packages (),

	install_requires = [
		'PyYAML>=3.12',
	],

	python_requires = '>=3',

	package_data = {
		'oijs.globals.config': [ 'default_conf/*.yml' ],
		'oijs.command.init': [ 'dir_structure/*.yml' ]
	},

	data_files = data_files,

	entry_points = {
		'console_scripts': [
			'oijs = oijs.main:main'
		]
	}
)
