# automation.py

# run `netstat -i` in a loop once every .1 sec for 1 sec in total duration (10 times)
# each time I run, I want to capture the # of tx, rx bytes/packets for one iface
# collection these measurements into a dictionary
#   { timestamp: { 'rx': 123, 'tx': 533 }, timestamp+1: ... }
# -> output as JSON

import subprocess
import datetime
import time
import json

if __name__ == '__main__':
    measurements = {}

    for _ in range(10):
        measurement = {}
        now = str(datetime.datetime.now())
        output = subprocess.check_output(['netstat', '-i'])
        for line in output.splitlines():
            if line.startswith('wlp4s0'):
                fields = line.split()
                iface, mtu, _, rx_ok, _, _, _, tx_ok, _, _, _, _ = fields
                measurement = {'iface': iface, 'rx': rx_ok, 'tx': tx_ok}
                measurements[now] = measurement
        time.sleep(.1)

    print json.dumps(measurements, indent=1)
