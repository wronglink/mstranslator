# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from mstranslator import AccessToken, AccessError, Translator

client_id = os.environ['TEST_MSTRANSLATOR_CLIENT_ID']
client_secret = os.environ['TEST_MSTRANSLATOR_CLIENT_SECRET']


class AccessTokenTestCase(unittest.TestCase):
    def test_access(self):
        at = AccessToken(client_id, client_secret)
        assert at.token

    def test_access_denied(self):
        at = AccessToken(client_id, "AN_INVALID_SECRET")
        self.assertRaises(AccessError, at.request_token)


class TranslatorTestCase(unittest.TestCase):
    def setUp(self):
        self.translator = Translator(client_id, client_secret)

    def test_translate(self):
        t = self.translator.translate('world', 'ru')
        self.assertEqual('мир', t)

    def test_get_langs(self):
        langs = self.translator.get_langs()
        self.assertIsInstance(langs, list)
        self.assertIn('en', langs)
