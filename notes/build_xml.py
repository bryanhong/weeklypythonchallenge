''' Goal:  Learn to Build XML Output

Build or Alterning XML
======================
e = Element(tag, attr=value, ...)
e.append(child_element)
e.remove(child_element)
e.text = sometext
e.tail = sometext

t = ElementTree(root)
t.write(file, encoding='utf-8', xml_declaration=True)

dump(e)                     # used for debugging

'''

from xml.etree.ElementTree import Element, ElementTree, dump
import csv

def add_element(parent, tag, text=None):
    e = Element(tag)
    parent.append(e)
    if text is not None:
        e.text = text
        e.tail = '\n'
    return e

directory = Element('directory', status='publicly visible', as_of='2015-07-29')
with open('notes/raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        person = add_element(directory, 'person')
        add_element(person, 'fullname', '%s %s' % (fname, lname))
        add_element(person, 'title', title)
        add_element(person, 'email_address', email)
        add_element(person, 'business_phone', phone)

tree = ElementTree(directory)
with open('raisins.xml', 'w') as f:
    tree.write(f, encoding='utf-8', xml_declaration=True) 





