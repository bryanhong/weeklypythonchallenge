import socket

host = 'www.jython.org'
port = 80
resource = '/'

request =  'GET %s HTTP/1.1\r\n' % resource
request += 'Host: %s\r\n' % host
request += 'Connection: close\r\n'
request += '\r\n' 

s = socket.socket()
try:
    s.connect((host, port))
    s.send(request)

    blocks = []
    while True:
        block = s.recv(4096)
        if len(block) == 0:
            break
        blocks.append(block)
    page = ''.join(blocks)
    
    print page.replace('\r\n', '\n')
finally:
    s.close()

