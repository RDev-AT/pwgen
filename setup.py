#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports
from setuptools import setup, find_packages


with open('requirements.txt', 'r', encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(name='pwgen',
      version='0.11',
      description='pwgen',
      url='https://github.com/RDev-AT/pwgen',
      author='RDev-AT',
      author_email='patrick.rehberger@rdev.at',
      license='GNU General Public License v3.0',
      packages=find_packages(),
      install_requires=requirements,
      setup_requires=['wheel'],
      zip_safe=False)

# build commands:
# python3 -m pip install --user --upgrade setuptools wheel
# python3 setup.py sdist bdist_wheel
