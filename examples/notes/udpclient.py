import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('The world is yours!', ('localhost', 9600))
s.close()

