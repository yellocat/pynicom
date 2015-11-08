#!/usr/bin/env python
import os
from setuptools import setup, find_packages
from pycom import __version__
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'pycom',
       version = __version__,
       description = 'A Minicom like shell in Python',
       long_description = read('README.md'),
       url='https://github.com/clobrano/pycom.git',
       author = 'Carlo Lobrano',
       author_email = 'c.lobrano@gmail.com',
       license = 'MIT',
       py_modules = ['pycom'],
       install_requires = ['docopt', 'raffaello'],
       packages = find_packages(),
       entry_points = {'console_scripts' : 'pycom = pycom:main'},
       keywords = ['serial', 'minicom'],
       classifiers = [
            "Development Status :: 4 - Alpha",
       ],
       )


