#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-modernizr',
    version='.'.join(map(str, __import__('modernizr').__version__)),
    author='David Gouldin',
    author_email='david@gould.in',
    url='http://github.com/dgouldin/django-modernizr',
    description = 'Django port of Marshall Yount\'s rack-modernizr',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)