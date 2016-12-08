# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='mstranslator',
    version='0.3.2',
    license='MIT',
    url='https://github.com/wronglink/mstranslator',
    bugtrack_url='https://github.com/wronglink/mstranslator/issues',
    description='Microsoft Translator API wrapper',
    long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
    author='Michael Elovskikh',
    author_email='wronglink@gmail.com',
    py_modules=['mstranslator'],
    install_requires=[
        'requests',
    ],
    tests_require=[
        'tox'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
