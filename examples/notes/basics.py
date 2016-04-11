'Quick tour of the Python language'

print 'My name is', __name__

if __name__ == '__main__':
    print 'Woohoo! I was run first'
    print 'This is called a main section'
    print 'We typically run test code here'
else:
    print 'Oh no!  I was run second'

# Type is called a list
foods = ['cake', 'cookies', 'jello']
print len(foods)       # sizeable
print foods[0]         # indexable
print foods
foods.append('ice cream')  # mutable
print foods

# Type:  tuple
person = ('Raymond', 'Hettinger', 0x32, 'python@rcn.com')
print len(person)
print person[1]
print person
# tuples are immutable == unchangeable == readonly

# Type:  number
x = 12
y = x             # assignments NEVER make copies
x += 1            # this makes a NEW number
print x
print y
# numbers are immutable

# Type:  set
colors = {'red', 'green', 'red', 'blue', 'green'}
print len(colors)
# sets eliminate duplicates
other_colors = {'green', 'brown', 'orange'}
print colors & other_colors
print colors | other_colors
print colors - other_colors
print other_colors - colors
# sets support classic: union intersection difference
print 'red' in colors
print 'yellow' in colors
# sets perform ultra-fast membership testing

# Type: dict
brand = {'raymond': 'mac',
         'james': 'thinkpad',
         'shah': 'lenovo'}

print brand['raymond']
print len(brand)
print brand.keys()
print brand.values()
print brand.items()
# dicts are called "unordered collections"
# because they don't remember insertion order
print 'james' in brand

# Type: str
s = 'the tale of two cities'
print len(s)
print s[0]
# str are immutable == unchangeable == readonly
# str methods create NEW strings
# you need to use them or save them
# casers:
print s.upper()
print s.lower()
print s.capitalize()
print s.title()
# aligners
print s.center(50)
print s.ljust(50)
print s.rjust(50)
print s.center(50, '=')
print s.ljust(50, '=')
print s.rjust(50, '=')
# predicates
print s.startswith('the')
print s.endswith('.html')
print s.islower()
print s.istitle()
print s.isdigit()
print s.isspace()
# torn-and-restored
t = s.split()
print t
print ''.join(t)
print ' '.join(t)
print ', '.join(t)
print ' <---> '.join(t)
print '_'.join(t)
print '\t'.join(t)
t = s.replace('two', 'three')
print t
# strippers
s = '   three  \t  blind    mice    \n'
print s.lstrip()
print s.rstrip()
print s.strip()
# invariant s[i:j] + s[j:k] == s[i:k]
#           (j - i) + (k - j) == k - i
s = 'the tale of two cities'
i = 2
j = 6
k = 9
print s[i:j] + s[j:k] == s[i:k]
print len(s[i:j]) == j - i
n = 8
print 'First eight characters:', s[:n]
print 'Last six characters:', s[-6:]

# Type:  function
def collatz(x):
    'Tool for verifying the Collatz conjecture'
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1

print type(collatz)
print dir(collatz)
print collatz(10)
print collatz(5)
print collatz.__name__, ' <-- Name at birth'
print collatz.__doc__
print repr(collatz.__code__.co_code)
print map(collatz, [10, 20, 30, 40, 50])

def myhelp(func):
    print 'Func name:', func.__name__
    print 'What is does:'
    print func.__doc__
    print

myhelp(hex)
myhelp(collatz)

# Type:  exceptions

e = KeyError('raymond')
print e
print type(e)

try:
    print 'Starting up'
    print 32 / 0
    print 'Finished'
except ZeroDivisionError:
    print 'Oh no, divide by zero'

class MyFunException(Exception):
    pass

try:
    print 'Do it again'
    raise MyFunException('we should go eat')
except MyFunException:
    print 'Okay we should finish the example first'

# Type:  classes and instances

class Computer:
    kind = 'Number computer machine'

    def __init__(self, brand):
        self.brand = brand

c = Computer('HP')
d = Computer('Apple')
e = Computer('Lenovo')

print c.kind
print d.kind
print c.brand
print d.brand

# Type:  files

with open('notes/queue_stats.txt') as f:
    data = f.read()
    print data

# Type: modules

import math

print math.pi
print math.cos(3.0)
print type(math)
print dir(math)

# Type:  urls

import urllib

u = urllib.urlopen('http://www.jython.org')
page = u.read()
print page[:50]
