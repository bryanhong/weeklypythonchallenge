# show_books.py

'''
    parse(filename or file-like-obj)    -> ElementTree document
    ET.getroot()                        -> root Element
    E.tag                               -> that element's tag
    E.attrib                            -> all the XML attributes (in a dict)
    E.get(attrib name)                  -> value for an XML attrib

    for child in E:                     -> all the immediate children of that Element
        print child

    E.find(xpath)                       -> find the first matching element
    E.findall(xpath)                    -> find all matching elements

XPATH:

    'tag'                      -> immediate child with the matching tag
    'tag/subtag'               -> immediate child of the immediate child with the matching subtag
    'tag//subtag'              -> any child of the immediate child

    '.'                        -> current element
    '..'                       -> parent element
    '*'                        -> all children

            '*[1]'              -> the first child (xpath counts starting from 1)
            '*[last()]'         -> the last child
            '*[pos() <=3]'      -> the first three children
            '*[@attr]'          -> the first child with this attr
            '*[@attr="value"]'  -> the first child with the matching attr/value pair
            '*[tag="text val"]' -> the first child with the matching text in the tag
'''

from xml.etree.ElementTree import parse
filename = 'notes/books.xml'

with open(filename) as f:
    catalog = parse(f).getroot()

print 'task 1: print all the book identifiers'

for book in catalog.findall('book'):
    print book.get('id')

print 'task 2: show all the book titles'

for title in catalog.findall('book/title'):
    print title.text

for book in catalog.findall('book'):
    print book.find('title').text

print 'task 3: show author, publication date of bk105'

book = catalog.find('book[@id="bk105"]')
print book.find('author').text, book.find('publish_date').text

print 'task 4: show author, price of all computer books'

for book in catalog.findall('book[genre="Computer"]'):
    print book.find('author').text, float(book.find('price').text)

print 'task 5: show all `metadata` for bk107'

for child in catalog.find('book[@id="bk107"]'):
    print child.tag.upper()
    print child.text
    print
    
