import json
import urllib
import urllib.parse
import urllib.request
import time
from pprint import pprint

with open('movietitles.txt') as f:
    titles = json.load(f)

titles = titles['titles']
results = []

for title in titles:
    encoded_title = urllib.parse.quote(title)
    tmdburl = 'https://api.themoviedb.org/3/search/movie?api_key=c6cae0cbe1d24c64b0ed91256178c0ac&language=en-US&query=' + encoded_title + '&page=1&include_adult=false'

    with urllib.request.urlopen(tmdburl) as url:
        time.sleep(1)
        data = json.loads(url.read().decode())
        print(f'---------------------')
        print(f'Title: {title}')
        if len(data['results']) > 0:
            for i, item in enumerate(data['results']):
                title = item['title']
                overview = item['overview']
                print(f'* Item #{i}: "{title}" - "{overview}"')
            print(f'---------------------')
            # correct_item = int(input("Index? "))
            results.append(data['results'][0])
        else:
            results.append({'Title': title})

with open('cleanmovies.json', 'w') as outfile:
    json.dump(results, outfile)
