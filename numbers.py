# numbers.py

from __future__ import division # "pragma": (makes the /-sign perform true division instead of floor division)

print 45 + 5
print 45 - 5
print 45 * 5
print 45 / 5

print 44 / 5 # int / int => int (*)
             # in Python 2, the default is to give an int (floor division)
             # in Python 3, the default is to give the actual result (true division)
             # in Python 2, use `from __future__ import division` (a pragma) to adopt the Python 3 default behavior

print 44 // 5 # always means explicit floor division

print 2 ** 10000 # Python has arbitrary-sied integers (automatic promotion)

print 44 % 3 # modulo: just the remainder
print 44 // 3 # just the dividend
print divmod(44, 3) # a tuple of the dividend, the remainder
print 44 // 3, 44 % 3
print abs(-41)
print oct(41)
print hex(41)
print bin(41)
print 41
print 0o51
print 0x29
print 0b101001

print 4 * 4.0
print 4 + 4.0
print 4 / 4.0
print int(4 * 4.2) # (int * float) => float -> int

print 1/3 * 3

print 11 + 22 == 33
print 1.1 + 2.2 == 3.3

print 4.0 == 4

print abs((1.1 + 2.2) - 3.3) < 0.1         # absolute threshold
print abs((1.1 + 2.2) - 3.3) < (0.1 * 3.3) # relative threshold

x = 1 + 4j
y = 2 + 3j

print x
print y
print x + y
print 3 * x
print x * y # (1+4j)(2+3j) == (2 + 8j + 3j + 12j*2) == (2 + 11j - 12)
print x + 2.0
print x + 2

print
print 'Average'

def average(seq):
    'average(seq) -> avwrage of the numbers in the seq'
    return sum(seq) / len(seq)

xs = [1,2,3,4,7, -10, -3-10j, 10.39]
print average(xs)

# "duck"-typed:
#   - if something looks like a duck
#   -              walks like a duck
#   -             quacks like a duck

print True, False

print type(10)
print type(10.0)
print type(10 + 1j)
print type(True)

print isinstance(10, int)
print isinstance(True, bool)
print isinstance(True, int)

xs = [True, True, False, False, True]
print sum(xs)
print average(xs)

# bitwise operators
print 1 << 2
print 1 >> 2
print -1 >> 2
print 5 ^ 3 # bitwise xor
print 5 & 3 # bitwise and
print 5 | 3 # bitwise or
print ~5    # bitwise not

x = 10
print id(x)
x += 1
print id(x)

x = x + 1
# x++
++x # this means (positive positive x) not (increment x)
--x # this means (negative negative x) not (decrement x)

# logical operators
print True and True
print True and False
print False or True
print False or False
print not True
print not False

x = 20
print x < 30
print x < 30 and x > 10
print 10 < x < 30

print 3 < x < 10 or x % 2 == 0



