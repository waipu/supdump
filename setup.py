#!/usr/bin/env python
from os.path import exists
from setuptools import setup
import supdump

setup(name='supdump',
      version=supdump.__version__,
      description='Supplementary code dump',
      url='https://github.com/waipu/supdump',
      author='waipu',
      author_email='waipu@cirno.de',
      license='GPL3',
      keywords='',
      packages=['supdump'],
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      zip_safe=False)
