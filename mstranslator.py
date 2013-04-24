# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta


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

    def request_token(self):
        data = dict(
            grant_type=self.grant_type,
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope=self.scope,
        )
        req = requests.post(self.access_url, data)
        resp = req.json()
        if req.status_code != 200:
            raise AccessError(resp['error_description'], resp['error'])
        self._token = resp['access_token']
        expires_in = int(resp['expires_in'])
        self._expdate = datetime.now() + timedelta(seconds=expires_in)

    @property
    def expired(self):
        return datetime.now() > self._expdate

    @property
    def token(self):
        if not self._token or self.expired:
            self.request_token()
        return self._token
