'Goal:  Parse an RSS feed to show the title of all the new items'

# http://rss.cnn.com/rss/cnn_topstories.rss
# notes/rss.xml

# Time box:  Aim for 5 minutes, maximum of 10

from xml.etree.ElementTree import parse
import urllib

def show_rss_titles(feed):
    'Show all the item titles in an RSS feed'
    rss = parse(feed).getroot()
    for title in rss.findall('channel/item/title'):
        print title.text

if __name__ == '__main__':
    show_rss_titles('notes/rss.xml')
    show_rss_titles(urllib.urlopen('http://rss.cnn.com/rss/cnn_topstories.rss'))

