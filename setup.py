#!/usr/bin/python
# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8

from setuptools import setup, find_packages
from dynamicLink import version
import os
#import sys
import shutil


# Read the version from a project file
VERSION = version.VERSION_str

# Get description from Readme file
readme_file = os.path.join(os.path.dirname(__file__), 'README.rst')
long_description = open(readme_file).read()

# To get the readme after installation with help(dynamicLink) copy the
# actual README in the project folder
readme_copy = os.path.join(os.path.dirname(__file__), 'dynamicLink', 'README_COPY')
try:
    shutil.copyfile(readme_file, readme_copy)
except IOError:
    pass

# Build a list with requirements of the app
REQUIRES = []
try:
    import django
except ImportError:
    # Because of the strange update behavior of "pip --upgrade package_name"
    # set requierment only if django not avallible.
    REQUIRES.append('django')

#if sys.version_info < (2, 4):
#    REQUIRES.append('python >= 2.4')


setup(name='django-dynamic-link',
        version=VERSION,
        description='A django file streaming application',
        long_description=long_description,
        author='Andreas Fritz',
        author_email='djangp-dynamic-link@bitzeit.eu',
        url='http://www.sources.e-blue.eu/de/pages/django/',
        download_url='https://bitbucket.org/catapela/django-dynamic-link/downloads',
        license='BSD',
        packages=find_packages(exclude=['example',]),
        include_package_data=True,
        keywords="django file streaming dynamic links serve",
        classifiers=[
              'Development Status :: 4 - Beta',
              'Framework :: Django',
              'License :: OSI Approved :: BSD License',
              'Operating System :: OS Independent',
              'Programming Language :: Python :: 2.4',
              'Environment :: Console',
              'Natural Language :: English',
              'Natural Language :: German',
              'Intended Audience :: Developers',
              'Topic :: Internet',
              ],
        install_requires = REQUIRES,
        zip_safe=False,
        )
