#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: setup.py

from setuptools import setup, find_packages

with open ( 'README.md', encoding='utf-8' ) as readme_file:
	long_description = readme_file.read ()

setup (
	name = 'oijs',
	version = '1.0.0',

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
		'oijs.globals.config': [ 'default_conf/*.yml' ]
	},

	data_files = [
		( 'share/doc/oijs', [ 'docs/README.md', 'docs/installation.md' ] ),
		( 'lib/oijs/oijs_dir', [ 'lib/oijs_dir/config.yml' ] ),
		( 'lib/oijs/init_dir/problem_dir', [ 'lib/init_dir/problem_dir/config.yml' ] )
	],

	entry_points = {
		'console_scripts': [
			'oijs = oijs.main:main'
		]
	}
)
