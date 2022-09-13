"""A setuptools based setup module for WG-Gesucht-Crawler-CLI"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    'beautifulsoup4==4.11.1',
    'certifi==2022.6.15',
    'chardet==5.0.0',
    'click==8.1.3',
    'idna==3.3',
    'requests==2.28.1',
    'urllib3==1.26.11',
]

setup(
    name='wg-gesucht-notifier',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Python web crawler / scraper for WG-Gesucht. Crawls the WG-Gesucht site for new apartment listings and send a message to the poster, based off your saved filters and saved text template.",
    long_description=readme,
    author="Hugo Melder",
    author_email='contact@hugomelder.com',
    url='https://github.com/hmelder/wg-gesucht-notifier',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts': [
            'wg-gesucht-notifier=wg_gesucht.cli:cli',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
