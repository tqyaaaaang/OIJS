#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: setup.py

from setuptools import setup

with open ( 'README.md', encoding='utf-8' ) as readme_file:
	long_description = readme_file.read ()

setup (
	name = 'oijs',
	version = '0.0.0.dev1',

	description = 'Judge System for OI and ACM',
	long_description = long_description,

	author = 'tqyaaaaang',
	author_email = 'tqyangoi1@gmail.com',

	keywords = 'oi judge',

	packages = [ 'oijs' ],

	install_requires = [
		'PyYAML'
	],

	python_requires = '>=3',

	entry_points = {
		'console_scripts': [
			'oijs = oijs.main:main'
		]
	}
)
