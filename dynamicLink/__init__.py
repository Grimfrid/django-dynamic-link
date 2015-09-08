import version
import os
import django
import sys
import django

__version__ = VERSION = version.VERSION
RELEASE_DJANGO = version.RELEASE_DJANGO
REQUIRES = version.REQUIRES

try:
    __doc__ = open(os.path.join(os.path.dirname(__file__), 'README_COPY')).read()
    __docformat__ = 'reStructuredText'
except IOError:
    __doc__ = 'For full documentation review the README file in your package or go to:' \
    'http://pypi.python.org/pypi/django-dynamic-link/'
    __docformat__ = 'txt'

def CKINST():
    """function to find problems of the installation."""
    print('I try to find errors for you!')
    
    djv = django.VERSION[:2]
    greatest_dlv = version.RELEASE_DJANGO[0]
    smalest_dlv = version.RELEASE_DJANGO[0]

    def strform(val):
        """returns formated version tuples"""
        return str(val).strip('()').replace(' ', '').replace(',','.')

    # find greatest and smallest possible django version for dynamic link
    for dlv in version.RELEASE_DJANGO:
        if greatest_dlv < dlv:
            greatest_dlv = dlv
        if smalest_dlv > dlv:
            smalest_dlv = dlv

    # Messages
    part1 = 'Warning! "django-dynamic-link %s" (use: "dynamicLink.VERSION") is not ' \
            'tested with "Django %s". May it runs with it may not! ' \
            'With the installed django-dynamic-link is "Django %s" recommended. ' \
            % (str(version.VERSION), str(django.VERSION), strform(greatest_dlv))
    part2 = 'Use "pip install django==%s.X". or downgrade django-dynamic-link. ' \
            % strform(greatest_dlv)
    part3 = 'Use "pip install django==%s.X" or try "pip install --upgrade django-dynamic-link". ' \
            % strform(greatest_dlv)
    part4 = 'To display all supported django versions in this release use "dynamicLink.RELEASE_DJANGO". ' \
            'To display recommended django-dynamic-link versions dynamicLink.REQUIRES'

    # check dynaic link dependences
    # Warnings
    warning = True
    if djv < smalest_dlv:
        print(part1)
        print(part2)
        print(part4)
    elif djv > greatest_dlv:
        print(part1)
        print(part3)
        print(part4)
    else:
        warning = False

    # Errors
    error = True
    pyver =  sys.version_info[:2]
    if pyver < version.PYTHON_MIN:
        print('')
        print('Error! Wrong python version. dynamicLink depends on python %s or higher. ' \
        'With this python installation dynamicLink will not work properly!' \
        % strform(version.PYTHON_MIN))
    else:
        error = False

    # check the python version for the actual django installation
    dja = django.VERSION[:2]
    hint = True
    if dja == (1,2) and not pyver >= (2,4):
        print('')
        print('Hint! Django %s requires Python 2.4 or greater.' % (dja,pyver))
    elif dja == (1,3) and not pyver >= (2,4):
        print('')
        print('Hint! Django %s requires Python 2.4 or greater.' % (dja,pyver))
    elif dja == (1,4) and not pyver >= (2,5):
        print('')
        print('Hint! Django %s requires Python 2.5 or greater.' % (dja,pyver))
    else:
        hint = False

    # success message
    if not error and not warning and not hint:
        print("No errors or warnings. All seems fine!")
