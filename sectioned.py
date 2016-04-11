# sectioned.py

import json

def parse_queue_stats(text):
    ''' parse the output of a `system internal qos queueing stats interface e1/10 command
        returning a list of dictionaries (one dict per queue) where each dictionary
        has ident, mode (tx, rx), total bytes, total packets '''
    qstats = []
    for line in text.splitlines():
        line = line.rstrip()
        if line.startswith(('Transmit', 'Receive')):
            mode, _ = line.split()
        elif line.lstrip().startswith('Queue'):
            _, ident = line.split()
            qstats.append({'ident': ident, 'mode': mode})
        elif 'total' in line.lower():
            fields = line.split()
            key  = ' '.join(fields[:-1])
            value = int(fields[-1])
            qstats[-1][key] = value
    return qstats

if __name__ == '__main__':
    filename = 'notes/queue_stats.txt'
    with open(filename) as f:
        text = f.read()
        qstats = parse_queue_stats(text)
        
    json_filename = filename.replace('.txt', '.json')
    with open(json_filename, 'w') as jf:
        jf.write(json.dumps(qstats, indent=1))

