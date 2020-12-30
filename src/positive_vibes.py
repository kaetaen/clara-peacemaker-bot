import requests
import json

class Requester:
    def __init__(self):
        self.base_url = 'https://positive-vibes-api.herokuapp.com'

    def request(self, path: str):
        response = requests.get(self.base_url + path)
        data = json.loads(response.content)

        print(data)


c = Requester()
c.request('/quotes/random')
