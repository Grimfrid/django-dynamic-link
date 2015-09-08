#!/usr/bin/python
# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8

VERSION = (0,5,6,2)
RELEASE_DJANGO = ((1,2),(1,3),(1,4))
PYTHON_MIN = (2,4)
REQUIRES ="""
django-dynamic-link 0.5.5 => Django 1.2, 1.3 :: Python >= 2.4 :: Example project: Django 1.3
django-dynamic-link 0.6.x => Django 1.2, 1.3, 1.4(Python 2.5) :: Python >= 2.4 :: Example project: Django 1.4, Python 2.5

(for an actual release visit http://pypi.python.org/pypi/django-dynamic-link/)
"""

APPLICATION_NAME = "Dynamic Link"
VERSION_str = str(VERSION[:3]).strip('()').replace(',','.').replace(' ','')
VERSION_INFO = """
Version: %s
Modification date: 03.08.2011

Hints:
- 0.5.6.2   settings.py in example project modified. Now it should work correct with Django 1.4
- 0.5.6.1   Timezone bug changes
- 0.5.6     Example Project runs with Django 1.4
- 0.5.5     dynamicLink.CKISNT() function added.
- 0.5.4.1   Canges in setup.py - READM will now alsow be installed. Now if a package
            is installed than help(dynamicLink) outputs the README.
- 0.5.4     Bugfix: Installation failed on Windows in spite of "/" on the end
            of recursive-include in MANIFEST. 
            Now canged from "recursive-include folder/ *" to "recursive-include folder *"
- 0.5.3     New stable release with updated readme.
- 0.5.2.2   structure of repository changed - src folder removed so readme is
            on the toplevel
- 0.5.2.1   In templates sentences changed.
- 0.5.2     stable - general django dependences in setup removed
- 0.5.1     new stable
- 0.5.0.2   some text in templates changed
- 0.5.0.1   correct readme and example settings.py
- 0.5.0     some changes - stable release
- 0.4.9.4   install_requires in setup.py modified
- 0.4.9.3   old data removed
- 0.4.9.2   dl_settings removed
- 0.4.9.1   Readme updatet
- 0.4.9     Testet with Django 1.2 u. 1.3
- 0.4.8.4   Some small changes
- 0.4.8.3   Some small changes
- 0.4.8     Runs now under Django 1.3
- 0.4.7   - Preesettings can now be overwrite in the presettings.py in the project
            folder, or directly in the global settings.py, or in a file
            called dl_settings.py in the same directory as manage.py.
            - django-dynamic-link now runs with python below version 2.6
- 0.4.6 -   changes in setup.py to avoid to install the example project.
- 0.4.5 -   Small adjustments at the example project.
- 0.4.4 -   1. Because of incomplete setup.py the last distributed package
            does't contained temples and language files.
            2. Readme updated.
            3. Example project added.
- 0.4.3 -   ImportError in admin.py solved.
- 0.4.2 -   setup.py createtd. Now listed in pypi.
- 0.4.1 -   Remove small bug with links created with the action menu.

TODO:
    - write more unittests
""" % (VERSION_str,)
