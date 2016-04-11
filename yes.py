# yes.py

import sys

if __name__ == '__main__':
    msg = sys.argv[1] if len(sys.argv) > 1 else 'y'
   
    while True:
        print msg
