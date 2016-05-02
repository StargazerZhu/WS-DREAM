#! /usr/bin/env python
'''
  Copyright (C) 2016, WS-DREAM, CUHK
  License: MIT

'''

description = 'WS-DREAM - A python package to benchmark QoS prediction approaches of Web services'

from distutils.core import setup, Extension
# from setuptools import setup, find_packages
import os
import os.path
import numpy
from distutils.sysconfig import *
# from distutils.util import *

try:
   from distutils.command.build_py import build_py_2to3 \
       as build_py
except ImportError:
   from distutils.command.build_py import build_py

try:
   from Cython.Distutils import build_ext
except ImportError:
   use_cython = False
else:
   use_cython = True

extra_compile_args = ['-O2']

#### data files
data_files = []

#### scripts
scripts = []

#### Python include
py_inc = [get_python_inc()]

#### NumPy include
np_inc = [numpy.get_include()]

#### cmdclass
cmdclass = {'build_py': build_py}

#### Extension modules
ext_modules = []
if use_cython:
    cmdclass.update({'build_ext': build_ext})
    ext_modules += [Extension("wsdream.PMF", 
                              ["wsdream/PMF/c_PMF.cpp",
                              "wsdream/PMF/PMF.pyx"],
                              language='c++',
                              include_dirs=py_inc + np_inc),
                    Extension("wsdream.NTF", 
                              ["wsdream/NTF/c_NTF.cpp",
                              "wsdream/NTF/NTF.pyx"],
                              language='c++',
                              include_dirs=py_inc + np_inc),
                    Extension("wsdream.UIPCC", 
                              ["wsdream/UIPCC/c_UIPCC.cpp",
                              "wsdream/UIPCC/UIPCC.pyx"],
                              language='c++',
                              include_dirs=py_inc + np_inc)
                              ]

else:
    ext_modules += [Extension("wsdream.PMF", 
                              ["wsdream/PMF/c_PMF.cpp",
                              "wsdream/PMF/PMF.cpp"],
                              include_dirs=py_inc + np_inc),
                    Extension("wsdream.NTF", 
                              ["wsdream/NTF/c_NTF.cpp",
                              "wsdream/NTF/NTF.cpp"],
                              include_dirs=py_inc + np_inc),
                    Extension("wsdream.UIPCC", 
                              ["wsdream/UIPCC/c_UIPCC.cpp",
                              "wsdream/UIPCC/UIPCC.cpp"],
                              include_dirs=py_inc + np_inc)
                              ]

packages=['wsdream']

classifiers = ['Intended Audience :: Science/Research',
               'License :: OSI Approved :: MIT',
               'Programming Language :: C++',
               'Programming Language :: Python',
               'Topic :: Scientific/Engineering :: Artificial Intelligence'
               ]

setup(name = 'wsdream',
      version='1.0',
      requires=['numpy (>=1.8.1)', 'scipy (>=0.13.3)'],
      description=description,
      author='WS-DREAM Team',
      author_email='wsdream.maillist@gmail.com',
      packages=packages,
      url='http://wsdream.github.io',
      download_url='https://github.com/wsdream/WS-DREAM',
      license='MIT',
      classifiers=classifiers,
      cmdclass=cmdclass,
      ext_modules=ext_modules,
      scripts=scripts,
      data_files=data_files
      )

print('==============================================')
print('Setup succeeded!\n')

