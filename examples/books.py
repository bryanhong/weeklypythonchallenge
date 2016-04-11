# books.py

import json

filename = 'notes/books.json'
with open(filename) as f:
    catalog = json.load(f)    

print 'task 1: show all the book identifiers'
for ident in sorted(catalog):
    print ident

print 'task 2: show the author and publication date of bk105'
book = catalog['bk105']
print book['author'], book['publish_date']

print 'task 3: show all the book titles'
for book in catalog.values():
    print book['title']

print 'task 4: show author and price of all computer books'

total_price = 0
for book in catalog.values():
    if book['genre'] == 'Computer':
        print book['price'], book['author']
        total_price += book['price']
print u'Total price: %.2f\N{rupee sign}' % total_price

print 'task 5: show all the meta-data for bk107 (author, desc, genre...)'

book = catalog['bk107']
for tag, text in book.items():
    print tag.upper()
    print text
    print



