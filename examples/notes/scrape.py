'Learn how to do screen scraping'

import urllib
import re

root_url = 'http://www.bhphotovideo.com/c/product/'

def comparison_shop(*products):
    'Compare current BH prices on various product codes'
    for product in products:
        url = root_url + product
        u = urllib.urlopen(url)
        page = u.read()
        mo = re.search(r'itemprop="price">\s*\$([0-9.]+)', page)
        print float(mo.group(1))

if __name__ == '__main__':
    comparison_shop('368226-REG', '93222-REG')
