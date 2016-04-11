# errors.py

def average(seq):
    return sum(seq) / len(seq)


xs = [1,2,3,4,10,20]
print average(xs)

xs = []
# print average(xs)

# Principle: don't handle errors unless we can do something meaningful about them

en_es = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres',
    'four': 'quatro',
    'five': 'cinco'
}

# looking before you leap (LBYL)
if 'six' in en_es:
    print 'six in Spanish is', en_es['six']
else:
    print "I don't know how to say 'six' in Spanish"

# it's better to ask for forgiveness than to ask for permission
try:
    print en_es['six']
except KeyError:
    print "I don't know how to say 'six' in Spanish!"

# Principle: ask forgiveness rather than permission (don't look before you leap)
# Principle: exceptions are NOT just for exceptional circumstances

KeyError
IndexError
ZeroDivisionError
SyntaxError
ImportError
MemoryError
TypeError
ValueError

try:
    # 10 / 0
    x = []
    x[0]
except ZeroDivisionError:
    print "You divided by zero!"
except IndexError:
    print "You looked for an index that didn't exist!"
except Exception: # rarely want to do this (how can you do something meaningful if you don't even know what kind of error?) ch
    print "You did something else wrong!"
except: # never want to do this! (will catch KeyboardInterrupt)
    print "You did something else wrong!"
