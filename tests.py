# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest
try:
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import BytesIO as StringIO

from mstranslator import AccessToken, AccessError, Translator

client_id = os.environ['TEST_MSTRANSLATOR_CLIENT_ID']
client_secret = os.environ['TEST_MSTRANSLATOR_CLIENT_SECRET']


class TranslatorMock(Translator):
    """
    A Translator mock that returns url on `.make_request()` method call without
    making a real HTTP request.
    """
    def make_request(self, action, params=None):
        return self.make_url(action, params)


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
        self.translator_mock = TranslatorMock(client_id, client_secret)

    def test_translate(self):
        t = self.translator.translate('world', 'ru')
        self.assertEqual('мир', t)

    def test_break_sentences(self):
        t = self.translator.break_sentences('Hello. How are you?', 'en')
        self.assertEqual(['Hello. ', 'How are you?'], t)

    def test_add_translation(self):
        url = self.translator_mock.add_translation('orig', 'trans', 'en', 'ru', user='test')
        self.assertIn('originalText=orig', url)
        self.assertIn('translatedText=trans', url)

    def test_get_langs(self):
        langs = self.translator.get_langs()
        self.assertIsInstance(langs, list)
        self.assertIn('en', langs)

    def test_get_lang_names(self):
        lang_names = self.translator.get_lang_names(['ru', 'en'], 'en')
        self.assertEqual(['Russian', 'English'], lang_names)

    def test_get_speackable_langs(self):
        langs = self.translator.get_langs(speakable=True)
        self.assertIsInstance(langs, list)
        self.assertIn('en-us', langs)

    def test_detect_lang(self):
        self.assertEqual('en', self.translator.detect_lang('Hello'))

    def test_speak(self):
        self.assertIsNotNone(self.translator.speak('Hello', 'en'))

    def test_speak_to_file(self):
        s = StringIO()
        self.translator.speak_to_file(s, 'Hello', 'en')
        s.seek(0)
        self.assertTrue(len(s.read()) > 0)
