# -*- coding: utf-8 -*-
import os
import codecs
from setuptools import setup

VERSION = '0.2.1'
ROOTDIR = os.path.dirname(__file__)
README = os.path.join(ROOTDIR, 'README.rst')

def run_tests():
    import sys, subprocess
    errno = subprocess.call([sys.executable, 'run_tests.py'])
    raise SystemExit(errno)


setup(
    name='pyCEO',
    version=VERSION,
    author='Juan-Pablo Scaletti',
    author_email='juanpablo@lucumalabs.com',
    packages=['pyceo'],
    package_data={
        'pyceo': [
            '*.py',
            '*.txt',
        ]
    },
    zip_safe=False,
    url='http://github.com/lucuma/pyCEO',
    license='MIT license (http://www.opensource.org/licenses/mit-license.php)',
    description='Create management scripts for your applications so you can do things like `python manage.py runserver`.',
    long_description=open(README,'r', 'utf-8').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='__main__.run_tests'
)
