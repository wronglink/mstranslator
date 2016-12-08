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

1. Subscribe to the Translator API
----------------------------------
To access Translator API you need a `Microsoft Azure`_ account. Note that subscriptions,
up to 2 million characters a month, are free. Translating more than 2 million characters per
month requires a payment.

2. Add Translator subscription to your Azure account
----------------------------------------------------
1. Select the **+ New** -> **Intelligence + analytics** -> **Cognitive Services APIs**.
2. Select the **API Type** option.
3. Select either **Text Translation** or **Speech Translation**.﻿Select the pricing tier that fits your needs.
4. Fill out the rest of the form, and press the **Create** button. You are now subscribed to Microsoft Translator.
5. Now retrieve your subscription key for authentication. You can find it in **All Resources** -> **Keys** option.

That's all. Now you have a Subscription Key and can use Microsoft Translator API.

Example Usage:

.. code-block:: pycon

    >>> from mstranslator import Translator
    >>> translator = Translator('<Subscription Key>')
    >>> print(translator.translate('Привет, мир!', lang_from='ru', lang_to='en'))
    Hello World!

Testing
=======
To run tests you need to set ``TEST_MSTRANSLATOR_SUBSCRIPTION_KEY`` environment variable
and install `tox`_ package. After that run shell command:

.. code-block:: console

    $ tox

.. _Microsoft Azure: http://azure.com
.. _tox: http://tox.readthedocs.org/en/latest/
