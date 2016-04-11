# show_queue_stats.py

''' goals: learn to parse column-orientated text data
           learn a preference for JSON/XML (REST APIs)
           - blank fields confound splitting and unpacking
           - fields containing whitespace confound splitting & unpacking
'''

import sys

if __name__ == '__main__':
    filename = 'notes/ipv4_int_bri.txt' if len(sys.argv) < 2 else sys.argv[1]
    
    with open(filename) as f:
        for lineno, line in enumerate(f, start=1):
            if lineno <= 2:
                continue
            
            fields = line.split()
            iface, ip, status, protocol = fields

            if 'down' not in status.lower(): # filter
                print '%-25s %16s' % (iface, ip) # projection
            
