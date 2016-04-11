# show_rss.py

'''
    parse(filename or a file-like obj)     -> ElementTree
    ET.getroot()                           -> root element
    E.tag                                  -> tag
    E.attrib                               -> all attrib (in a dict)
    E.text                                 -> the enclosed text
    E.get(attrib name)                     -> value for that XML attrib

    for chlid in E:                        -> loop over the children
        print child

    E.find(xpath)                          -> first matching element
    E.findall(xpath)                       -> list all matching elements
    
'''

from xml.etree.ElementTree import parse

filename = 'notes/rss.xml'
with open(filename) as f:
    doc = parse(f)
root = doc.getroot()

# print out the title and publication date for each news item

for item in root.findall('channel/item'):
	print item.find('title').text, item.find('pubDate').text

# rss
#  \___ channel
#          |------ item
#                    \_ title, pubDate
#          |------ item
#                    \_ title, pubDate
#          |------ item
#                    \_ title, pubDate
#          |------ item
#                    \_ title, pubDate
