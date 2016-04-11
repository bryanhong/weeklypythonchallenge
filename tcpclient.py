# tcpclient.py

from socket import socket
from json import dumps, loads

sock = socket()
sock.connect(('171.69.52.97', 9000))
sock.send(dumps({
    'game': 'crossword',
    'entry': 'p_th_n'
}))

print sock.recv(2**10)
