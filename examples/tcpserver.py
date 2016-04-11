# tcpserver.py

from socket import socket
from socket import SOL_SOCKET, SO_REUSEADDR
from crossword import (find_crossword_candidates,
                       find_jumble_candidates,
                       find_scrabble_candidates,
                       load_wordlist)
from json import loads, dumps

sock = socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sock.bind(('171.69.52.97', 9000))
sock.listen(15)

wordlist = load_wordlist()

while True:
    conn, who = sock.accept()
    ip, port = who
    msg = conn.recv(1024)

    try:
        cmd = loads(msg)
        game = cmd['game']
        entry = cmd['entry']
    except Exception as e:
        response = {'error': str(e)}
        conn.sendall(dumps(response))
        print e
        continue

    response = {}
    if game == 'crossword':
        response['answer'] = list(find_crossword_candidates(wordlist, entry))

    conn.sendall(dumps(response))
