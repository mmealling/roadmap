import json
import urllib
import urllib.parse
import urllib.request
import time
from isbnlib import isbn_from_words
from isbnlib import meta
from isbnlib import cover
from isbnlib import desc
from pprint import pprint
from random import randint


with open('booktitles.json') as f:
    books = json.load(f)

books = books['books']
results = []

for book in books:
    isbn = isbn_from_words(book['author'] + " " + book['title'])
    print("for ", book['title'], " the isbn is ", isbn)
    try:
        metadata = meta(isbn, service='default', cache=None)
    except:
        metadata = {}

    images = cover(isbn)
    description = desc(isbn)
    book['isbn'] = isbn
    book['metadata'] = metadata
    book['desc'] = description
    book['cover'] = images
    results.append(book)
    with open('cleanbooks.json', 'w') as outfile:
        json.dump(results, outfile)

    time.sleep(randint(10,60))