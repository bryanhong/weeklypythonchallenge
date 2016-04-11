'Goal:  Practice JSON parsing and practice core dictionary skills'

import json

with open('notes/books.json') as f:
    catalog = json.load(f)

print 'Task 1:  List all the book identifiers'
for key in sorted(catalog):
    print key

print 'Task 2:  Show all the book titles'
for book in catalog.values():
    print book['title']
    
print 'Task 3:  Author and Pub date of bk105'
book = catalog['bk105']
print book['author'], '-->',
print book['publish_date']

print 'Task 4:  Author and price of computer books'
for book in catalog.values():
    if book['genre'].lower() == 'computer':
        print book['author'], '-->',
        print book['price']

print 'Task 5:  Show all metadata for bk107'
book = catalog['bk107']
for tag, tagvalue in book.items():
    print tag.upper()
    print tagvalue
    print
