# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='mstranslator',
    version='0.1',
    license='MIT',
    description='Microsoft Translator Api wrapper',
    author='Michael Elovskikh',
    author_email='wronglink@gmail.com',
    py_modules=['mstranslator'],
    install_requires=[
        'requests',
    ],
    tests_require=[
        'tox'
    ],
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ),
)