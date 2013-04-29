# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from datetime import datetime, timedelta
try:
    # Python 3
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    import simplejson as json
except ImportError:
    import json
try:
    basestring
except NameError:
    basestring = (str, bytes)


class AccessError(Exception):
    def __init__(self, message, error):
        self.error = error
        super(AccessError, self).__init__(message)


class AccessToken(object):
    client_id = ""
    client_secret = ""
    access_url = "https://datamarket.accesscontrol.windows.net/v2/OAuth2-13"
    scope = "http://api.microsofttranslator.com"
    grant_type = "client_credentials"

    _token = None
    _expdate = None

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def __call__(self, r):
        r.headers['Authorization'] = "Bearer " + self.token
        return r

    def request_token(self):
        data = dict(
            grant_type=self.grant_type,
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope=self.scope,
        )
        resp = requests.post(self.access_url, data)
        d = resp.json()
        if resp.status_code != 200:
            raise AccessError(d['error_description'], d['error'])
        self._token = d['access_token']
        expires_in = int(d['expires_in'])
        self._expdate = datetime.now() + timedelta(seconds=expires_in)

    @property
    def expired(self):
        return datetime.now() > self._expdate

    @property
    def token(self):
        if not self._token or self.expired:
            self.request_token()
        return self._token


class Translator(object):
    api_url = "http://api.microsofttranslator.com/V2/Ajax.svc/"

    def __init__(self, client_id, client_secret):
        self.auth = AccessToken(client_id, client_secret)

    def make_url(self, action, params=None, ):
        url = self.api_url + action
        if params:
            url += '?' + urlencode(params)
        return url

    def make_request(self, action, params=None):
        url = self.make_url(action, params)
        resp = requests.get(url, auth=self.auth)
        return self.make_response(resp)

    def make_response(self, resp):
        # Sanitize strange zero width no-break space character in response
        text = resp.text.replace('\ufeff', '')
        return json.loads(text)

    def translate(self, text, lang_to, lang_from=None, contenttype='text/plain', category='general'):
        if contenttype not in ('text/plain', 'text/html'):
            raise ValueError('Invalid contenttype value')
        params = {
            'text': text,
            'to': lang_to,
            'contentType': contenttype,
            'category': category,
        }
        if lang_from:
            params['from'] = lang_from
        return self.make_request('Translate', params)

    def get_langs(self, speakable=False):
        action = 'GetLanguagesForSpeak' if speakable else 'GetLanguagesForTranslate'
        return self.make_request(action)

    def detect_lang(self, text):
        return self.make_request('Detect', {'text': text})

    def speak(self, text, lang, format='audio/wav', best_quality=False):
        if format not in ('audio/wav', 'audio/mp3'):
            raise ValueError('Invalid format value')
        params = {
            'text': text,
            'language': lang,
            'format': format,
            'options': 'MaxQuality' if best_quality else 'MinSize',
        }
        return self.make_request('Speak', params)

    def speak_to_file(self, file, *args, **kwargs):
        resp = requests.get(self.speak(*args, **kwargs))
        if isinstance(file, basestring):
            with open(file, 'wb'):
                file.write(resp.content)
        elif hasattr(file, 'write'):
            file.write(resp.content)
        else:
            raise ValueError('Expected filepath or a file-like object')