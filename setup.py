#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The setup script
"""

from setuptools import (
    setup,
    find_packages
)


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changes:
    changelog = changes.read()

# TODO: read dependencies from Pipfile
requirements = ['flask']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    name='car-api',
    version='0.1.0',
    keywords='car-api',
    description="A sample car api",
    long_description=readme + '\n\n' + changelog,
    author="Franco Riberi",
    author_email='fgriberi@gmail.com',
    url='https://github.com/ogli-api/car-api',
    zip_safe=False,
    install_requires=requirements,
    license="",
    include_package_data=True,
    packages=find_packages(include=['car_api']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'car-api=car_api.app:main',
        ],
    },
)
