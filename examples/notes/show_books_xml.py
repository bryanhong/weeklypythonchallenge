''' Goal:  Learn a very useful subset of XML parsing capabilities.

from xml.etree.ElementTree import parse

parse(filename or file-like object)    -> ElementTree
ET.getroot()                           -> The Root Element
E.tag                                  -> The first word in the opener
E.text                                 -> The words between the opener and closer
E.get(attr)                            -> Looks up the attribute in the opener and finds the value
E.attrib                               -> Dictionary of all the attribute value pairs
E.find(xpath)                          -> First matching subelement
E.findall(xpath)                       -> List of matching subelements
for se in E:                           -> Loops over all children (no matching)

XPath Notation (standard):
tag                        Immediate Child with a matching tag
tag/subtag                 Immediate child of an immediate child
tag//subtag                Any level of descendant of an immediate child
*                          All immediate children
.                          Current element
..                         Parent element (but in ElementTree, no higher than you started
[1]                        Index to the first child (counts from one)
[@attr]                    First child that has a given attribute
[@attr="value"]            First child with a matching attribute/value pair
[tag="text_value"]         First child with a given tag that has EXACTLY matching text
[last()]                   Last child
[pos() <= 3]               Matches the first three children

'''

from xml.etree.ElementTree import parse

catalog = parse('notes/books.xml').getroot()

print 'Task 1:  List all the book identifiers'
for book in catalog:
    print book.get('id')

print 'Task 2:  Show all the book titles'
for title in catalog.findall('book/title'):
    print title.text

print 'Task 3:  Author and Pub date of bk105'
book = catalog.find('book[@id="bk105"]')
print book.find('author').text, '-->',
print book.find('publish_date').text

print 'Task 4:  Author and price of computer books'
for book in catalog.findall('book[genre="Computer"]'):
    print book.find('author').text, '-->',
    print book.find('price').text    

print 'Task 5:  Show all metadata for bk107' 
for metadata in catalog.find('book[@id="bk107"]'):
    print metadata.tag.upper()
    print metadata.text
    print
