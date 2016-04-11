import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 9600))
try:
    while True:
        msg, who = s.recvfrom(256)
        print msg, who
finally:
    s.close()

