# -*- coding: utf-8 -*-
"""starships-of-war setup.py"""

from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='starships-of-war',
    version='0.1.0',
    description='a cli application to rank starwars starships',
    long_description=readme(),
    license='MIT',
    author='Matheus Heck',
    author_email='matheus@conduite.tv',
    keywords='python basic cli reading postgres',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.>4',
        'Topic :: Utilities',
    ],
    url='https://github.com/matheusheck/starships-of-war',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'SQLAlchemy',
        'psycopg2'
    ],
    entry_points={
        'console_scripts': [
            'starships-of-war = starships_of_war:cli.run',
        ],
    },
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
)
