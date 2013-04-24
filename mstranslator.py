# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta
from urllib import urlencode
try:
    import simplejson as json
except ImportError:
    import json


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
