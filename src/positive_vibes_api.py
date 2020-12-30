import requests
import json

class Requester:
    def __init__(self):
        self.base_url = 'https://positive-vibes-api.herokuapp.com'

    def request(self, path: str):
        url = self.base_url + path

        if 'quotes' in url:
            data = requests.get(url).content
            content = json.loads(data)
            
            return content['msg']
        
        if 'songs' in url:
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
