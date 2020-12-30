from typing import Any
import requests
import json
from requests.models import Response

class Requester:
    def __init__(self):
        self.base_url = 'https://positive-vibes-api.herokuapp.com'

    def request(self, path: str):
        url = self.base_url + path
        data = requests.get(url).content
        content = json.loads(data)

        if 'quotes' in url:
            return content
        else:
            return url


class Quotes(Requester):
    def randomQuote(self):
        quote = self.request('/quotes/random')
        return quote


class Music(Requester):
    def randomMusic(self):
        music = self.request('/songs/random')

        return music


class Images(Requester):
    ...
