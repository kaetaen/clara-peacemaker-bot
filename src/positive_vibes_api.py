import requests
import json

class Requester:
    def __init__(self):
        self.base_url = 'https://positive-vibes-api.herokuapp.com'

    def request(self, path) -> dict:
        response = requests.get(self.base_url + path)
        data = json.loads(response.content)

        return data


class Quotes(Requester):
    def randomQuote(self) -> str:
        quote: dict = self.request('/quotes/random')
        
        return quote["msg"]
