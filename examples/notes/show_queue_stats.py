'Goal:  Learn to parse sectioned reports typical for Cisco'


def parse_qstats(text):
    ''' Parse the output of: 'system internal qos queuing stats interface e1/10'
        Return a list of dictionarys, one per queue.
    '''
    qstats = []
    mode = ''
    for line in text.splitlines():
        line = line.strip().lower()
        if line.startswith(('receive', 'transmit')): # At the start of a new mode, save the mode in a global
            mode, _ = line.split()
        if 'drops' in line or line.startswith(('total bytes', 'total packets', 'queue')):
            fields = line.split()
            key = ' '.join(fields[:-1])              # The key is all of the fields except the last
            value = fields[-1]                       # The value of interest is in the last field
            if key == 'queue':                       # At start of a new queue section, create a new dict
                qstat = {'mode': mode}
                qstats.append(qstat)                 # Add the new queue dict to the list of queues
            qstat[key] = value                       # Inside a queue section, store the key/value pairs
    return qstats

if __name__ == '__main__':
    import json

    with open('notes/queue_stats.txt') as f:
        output = f.read()

    qstats = parse_qstats(output)
    print json.dumps(qstats, indent=2)    
