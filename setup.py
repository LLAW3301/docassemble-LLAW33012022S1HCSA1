import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012022S1HCSA1',
      version='1',
      description=('HSCA application'),
      long_description='# docassemble.LLAW33012022S1HCSA1\r\n\r\n\r\n\r\n## Author\r\n\r\nMatthew Gunn, gunn0065@flinders.edu.au\r\nCaitlin Bishop, bish0174@flinders.edu.au\r\nCaitlin Aldous, aldo0077@flinders.edu.au\r\nTara Nuttall, nutt0019@flinders.edu.au\r\nMarteenah Abdalah Shonoodh, marteenah.abdalahshonoodh@flinders.edu.au\r\nDaniel Hill-Brown, hill0626@flinders.edu.au\r\n\r\n## Description\r\nThis is an appplication designed to help Housing Choices South Australia tenants who are experiencing anti-social behaviour in their community find appropriate resolution pathways.',
      long_description_content_type='text/markdown',
      author='Matthew Gunn',
      author_email='gunn0065@flinders.edu.au',
      license='',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012022S1HCSA1/', package='docassemble.LLAW33012022S1HCSA1'),
     )

