''' Write a UDP battleship game.
    Figure-out how you would play it by mail.

Rules:
    https://en.wikipedia.org/wiki/Battleship_%28game%29

Photo of game board:
    http://blogs-images.forbes.com/erikkain/files/2012/02/battleship-board-game.jpg

Data structure:

        >>> ships = {'B4', 'B5', 'B6', 'G5', 'H5', 'I5', 'J5'}
        >>> guess = 'C2'
        >>> if guess in ships:
                print 'Hit!'
        else:
                print 'Miss!'

Command-line args:
        import sys
        print sys.argv

Blue Computer API (server)
--------------------------
$ python battleship.py B4 B5 B6 G5 H5 I5 J5
listening for an attacker on localhost:9600
Incoming:  C2       Miss!
Incoming:  B5       Hit!


Red Computer API (client)
-------------------------
$ python shoot.py C2
Miss!
$ python shoot.py B5
Hit!

Solutions (don't peek):
-----------------------
https://dl.dropboxusercontent.com/u/3967849/battleship/pub/index.html

TCP Version
===========

Blue Computer API (server)
--------------------------
$ python bs_tcp.py B4 B5 B6 G5 H5 I5 J5
Incoming:  C2       Miss!
Incoming:  B5       Hit!

Red Computer
------------
$ telnet localhost 9600
T: [Connected]
C: C2
S: Miss!
C: B5
S: Hit!
C: quit
[Connection closed by foreign host]

Tools
-----
s.settimeout(2)
f = s.makefile()
f.write('C2\r\n')
f.readline()

'''
