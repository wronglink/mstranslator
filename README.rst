==============================================
mstranslator: Microsoft Translator API wrapper
==============================================

.. image:: https://travis-ci.org/wronglink/mstranslator.png?branch=master
   :target: https://travis-ci.org/wronglink/mstranslator
   :alt: Travis-ci: continuous integration status.

.. image:: https://badge.fury.io/py/mstranslator.png
   :target: http://badge.fury.io/py/mstranslator
   :alt: PyPI version

Installation
============

Install with pip:

.. code-block:: console

    $ pip install mstranslator

Usage
=====

1. Subscribe to the Microsoft Translator API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Subscribe to the `Microsoft Translator dataset`_ on Azure Marketplace. Note that subscriptions,
up to 2 million characters a month, are free. Translating more than 2 million characters per
month requires a payment.

2. Register an application
~~~~~~~~~~~~~~~~~~~~~~~~~~
Register an application `here`__. As the redirect field is not used but it's marked as required
you may enter any URI to pass validation.

That's all. Now you have a Client ID and Client secret.

Example Usage:

.. code-block:: pycon

    >>> from mstranslator import Translator
    >>> translator = Translator('<Client ID>', '<Client secret>')
    >>> print(translator.translate('Привет, мир!', lang_from='ru', lang_to='en'))
    Hello World!

Testing
=======
To run tests you need to set ``TEST_MSTRANSLATOR_CLIENT_ID`` and ``TEST_MSTRANSLATOR_CLIENT_SECRET`` environment variables
and install `tox`_ package. After that run shell command:

.. code-block:: console

    $ tox

.. __: https://datamarket.azure.com/developer/applications/
.. _Microsoft Translator dataset: https://datamarket.azure.com/dataset/bing/microsofttranslator
.. _tox: http://tox.readthedocs.org/en/latest/
