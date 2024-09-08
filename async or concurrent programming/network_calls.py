import requests
import time

start_time = time.time()

def sync_fetch(url):
    return requests.get(url).text

# page1 = sync_fetch('https://pokeapi.co/api/v2/pokemon?limit=10&offset=0')
# page2 = sync_fetch('https://pokeapi.co/api/v2/pokemon?limit=10&offset=1000')
