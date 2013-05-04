# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='mstranslator',
    version='0.2.1',
    license='MIT',
    url='https://github.com/wronglink/mstranslator',
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
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ),
)
