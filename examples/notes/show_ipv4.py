''' Goal:  Learn to parse column-oriented text meant for humans
           such as the output from the Cisco IOS

    Command:  # show ipv4 interfaces brief

    Also teach why this slow and fragile.  Build a strong preference for REST APIs with JSON/XML.
    * Blank fields will confound splitting and unpacking.
    * Fields that contain whitespace also confound splitting and unpacking.

'''

with open('notes/ipv4_int_bri.txt') as f:
    for line in f:
        # line = line.rstrip()
        # interface, ipaddr, status, protocol = line.split()
        interface = line[:31].rstrip()
        ipaddr = line[31:47].rstrip()
        status = line[47:69].rstrip()
        protocol = line[69:].rstrip()
        
        if status.lower() == 'up':
            print '%-15s %s' % (ipaddr, interface)

        
