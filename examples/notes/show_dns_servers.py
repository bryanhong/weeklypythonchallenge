'Goal:  Learn that JSON is a superior data interchange format'

import json

with open('notes/dns_servers.json') as f:
    response = json.load(f)

for dns_server in response['items']:
    print '%(ip-address)-15s primary status is %(primary)s' % dns_server

