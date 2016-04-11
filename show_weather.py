# show_weather.py

import urllib
from xml.etree.ElementTree import parse
import time

root_url_template = 'http://w1.weather.gov/xml/current_obs/%s.xml'

if __name__ == '__main__':
    locations = 'KSJC', 'KJFK', 'KEWR', 'KDFW', 'KSFO'

    for _ in range(10):
        for location in locations:
            url = root_url_template % location
            u = urllib.urlopen(url)
            root = parse(u).getroot()

            temp_f = float(root.find('temp_f').text)
            humidity = float(root.find('relative_humidity').text)

            print 'At %s' % location
            print u'\ttemp:     %.2f\N{degree fahrenheit}' % temp_f
            print  '\thumidity: %.2f%%' % humidity
        time.sleep(.1)
