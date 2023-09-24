import requests
import json

class PositiveVibesAPI:
    def __init__(self):
        self.base_url = 'https://positive-vibes-6xte.onrender.com'
    
    def request(self, path: str):
        url = self.base_url + path
        data = requests.get(url).content
        content = json.loads(data)
            
        return content['data']

    def get_music(self):
        music = self.request('/songs/random')
        data_music = {
            "artist_name": music["artist_name"],
            "song_name": music["name"],
            "file": music["audio"]
        }   

        return data_music

    def get_quote(self):
        quote = self.request('/quotes/random')
        
        return quote

    def get_image(self):
        image = self.request('/images/random')

        return image

    def get_podcast(self):
        episode = self.request('/podcasts/random')
        
        return episode


