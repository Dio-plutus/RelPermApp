# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup
from os import path
import re


def find_version():
    here = path.abspath(path.dirname(__file__))
    absfn = path.join(here, 'appmode/__init__.py')
    content = open(absfn).read()
    match = re.search(r"\n__version__ = ['\"]([^'\"]+)['\"]", content)
    return match.group(1)


setup(
    name='appmode',
    license='MIT',
    version = find_version(),
    author = 'Ole Schuett',
    author_email = 'ole.schuett@cp2k.org',
    url='http://github.com/oschuett/appmode',
    description='A Jupyter extensions that turns notebooks into web applications.',

    packages=["appmode"],
    include_package_data = True,
    install_requires=['notebook>=5'],
    data_files=[('share/jupyter/nbextensions/appmode', [
                    'appmode/static/main.js',
                    'appmode/static/gears.svg'
    ])],


#EOF
