import json
import urllib
import urllib.parse
import urllib.request
import time
import psycopg2
from datetime import date
from pprint import pprint

conn = psycopg2.connect("dbname=roadmap")
cursor = conn.cursor()
with open('cleanbooks.json') as f:
    books = json.load(f)

books = books["books"]

results = ''

for book in books:
        # {
        #     "author": "Brian Aldiss",
        #     "cover": {
        #         "smallThumbnail": "http://books.google.com/books/content?id=rLnyAAAAMAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
        #         "thumbnail": "http://books.google.com/books/content?id=rLnyAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        #     },
        #     "desc": "In the distant future of galactic empires, the people of the Greene-tribe\nare shocked when they discover that they are not the center of a world of\ntheir own making, in a new edition of the classic science fiction novel,\nfirst published in 1958. Reprint.",
        #     "isbn": "9781585676835",
        #     "metadata": {
        #         "Authors": [
        #             "Brian Wilson Aldiss"
        #         ],
        #         "ISBN-13": "9781585676835",
        #         "Language": "en",
        #         "Publisher": "",
        #         "Title": "Non-Stop",
        #         "Year": "2005"
        #     },
        #     "title": "Starship"
        # },
    mybook = {}
    mybook["isbn"] = book["isbn"]
    mybook["title"] = str(book["title"])
    mybook["description"] = book["desc"]
    mybook["picture"] = json.dumps(book["cover"])
    metadata = book["metadata"]

    print(f'foo')

    if 'Year' in metadata:
        release_date = date(int(book["metadata"]["Year"]),1,1)
        mybook["release_date"] = release_date
    else:
        mybook["release_date"] = None
    
    if "Authors" in book["metadata"]:
        mybook["authors"] = json.dumps(book["metadata"]["Authors"])
    else:
        mybook["authors"] = json.dumps(book["author"])
    
    print(f'title:{mybook["title"]}   isbn: {mybook["isbn"]}')

    results += cursor.mogrify("insert into dependency_book (title, isbn, description, thumbnail, release_date, authors) values (%(title)s, %(isbn)s, %(description)s, %(picture)s, %(release_date)s, %(authors)s);", mybook).decode('utf-8')
    results += '\n'

with open('newbooks.sql', 'w') as outfile:
    outfile.write(results)
