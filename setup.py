#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: setup.py


"""
module setup
"""


import os
import glob
from pathlib import Path
from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as readme_file:
    long_description = readme_file.read()   # pylint: disable=C0103


def get_all_files(src: Path, dst: Path):
    """
    get_all_files
    """

    src = Path(src)
    dst = Path(dst)

    cur_files = os.listdir(str(src))
    in_src = []
    cur_data_files = []
    for element in cur_files:
        if (src / element).is_file():
            in_src.append(str(src / element))
        else:
            cur_data_files.extend(get_all_files(
                src / element, dst / element
            ))
    if in_src:
        cur_data_files.append((str(dst), in_src))
    return cur_data_files


def get_package_data(pattern):
    data = glob.glob('oijs/' + pattern, recursive=True)
    return list(map(lambda x: x[5:], data))


# pylint: disable=C0103
data_files = get_all_files('docs/', 'share/doc/oijs/')

# pylint: disable=C0103
package_data = get_package_data('**/*.yml')


setup(
    name='oijs',
    version='1.1.0',

    description='Judge System for OI and ACM',
    long_description=long_description,

    author='tqyaaaaang',
    author_email='tqyangoi1@gmail.com',

    keywords='oi judge',

    packages=find_packages(),

    install_requires=[
        'PyYAML>=3.12',
        'wrapt>=1.10',
        'importlib_resources>=1.0.2'
    ],

    python_requires='>=3.5',

    package_data={
        'oijs': package_data
    },

    data_files=data_files,

    entry_points={
        'console_scripts': [
            'oijs = oijs.__main__:main'
        ]
    }
)
