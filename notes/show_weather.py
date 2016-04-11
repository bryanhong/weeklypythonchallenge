# Parse a live weather feed from NOAA information for San Jose weather
# http://w1.weather.gov/xml/current_obs/KSJC.xml
# --> current temperature and relative humidity

# Time box: aim for 5 minutes, max of 10 minutes.

import urllib
from xml.etree.ElementTree import parse

def current_observation(station='KSJC'):
    'Display the temperature and relative humidity at aviation observation station'
    url_template = 'http://w1.weather.gov/xml/current_obs/%s.xml'
    url = url_template % station
    u = urllib.urlopen(url)

    curr_obs = parse(u).getroot()
    temperature = curr_obs.find('temp_f').text
    humidity = curr_obs.find('relative_humidity').text

    print u'At the %s station, the temperature is %s\N{degree sign}F' % (station, temperature),
    print 'and the relative humidity is %s%%.' % humidity

if __name__ == '__main__':
    current_observation('KSJC')
    current_observation('KSEA')    
