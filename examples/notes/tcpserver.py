import socket, time

s = socket.socket()
s.bind(('', 9601))
s.listen(5)
print 'Server up, running, and waiting for call'
try:
    while True:
        c, a = s.accept()
        print "Received connection from", a
        c.sendall("Hello %s\r\n" % a[0])
        c.sendall("The time is %s\r\n" % time.ctime())
        c.close()
finally:
    s.close()
