# any_and_all.py

from __future__ import division

print True
print False

print bool(True)
print bool(False)

print bool(0)
print bool(1)

print bool([])

xs = [1,1,2]
xs.remove(1)
xs.remove(2)

print bool(xs)

xs = {1,1,2}
xs.remove(1)
xs.remove(2)

print bool(xs)

xs = 1, 1, 2
# xs.remove(1)  # can't REMOVE elements from a tuple -> tuple is immutable
# xs.remove(2)

print bool(xs)

print bool(''), bool([''])

print bool(()), bool((())), bool(((),))

print all(['', False, 0])

print any(['okay', True, 3.3 - 2.2 - 1.1])

print any([[], '', ([],)])

print any([0.0, False, set(), 1//3])

x = y = []


print all([ {123: 123}, ((),), x is y ])


x.append(1)

print bool(1 in y)


x, y = [], []
z = x

print x is y, x is z, x == y, x == z

#    id(x) == id(y)    (ALWAYS  implies)      x is y
#    x == y            (NEVER   implies)      x is y
#    x is y            (USUALLY implies)      x == y 

class Foo(object):
    def __eq__(self, other):
        return False

x = Foo()

print bool(len([]))

print bool(len)
'
def f():
    return False

if f():
    print 'hello!'

mutable = {list, dict, set}
immutable = {str, int, float, complex, bool, tuple, frozenset}

types = list(mutable | immutable)

from random import choice
for _ in range(10):
    print 'Why would I choose a %r over a %r?' % (choice(types), choice(types))

    
















