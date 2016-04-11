# starschool.py

def f(x):
    'returns the square of x'
    return x ** 2

def f(x):
    return x, x ** 2

result = f(10)
a, b = f(10)

def f(x):
    'returns None'
    
def f(x):
    pass

def f(x):
    return

def f(x):
    return None

def f(x, y=10):
    print 'x =', x
    print 'y =', y
    return x, y

f(1,2)
f((1,2))
f(((1,2)))

print 'star-args'.center(80, '-')

def f(xs):
    print 'f(xs)'.center(50, '=')
    for i, x in enumerate(xs):
        print 'xs[%d] = %s' % (i, x)

f([10, 20, 30])
f((10, 20, 30, 40, 50, 60))

def f(*xs):
    print 'f(*xs)'.center(50, '=')
    for i, x in enumerate(xs):
        print 'xs[%d] = %s' % (i, x)

f('a')
f('a', 'b', 'c')
f('a', 'b', 'c', 'd')

f(('a', 'b', 'c'))

f(['a', 'b', 'c'], ['d', 'e', 'f'], ('h', 'i', 'j'))

# def f(*xs):
#   pass
# means that f takes MULTIPLE POSITIONAL arguments
#   -> packed into a TUPLE

def f(x, y=1, z=2):
    print 'f(x, y=1, z=2)'.center(50, '=')
    print 'x =', x
    print 'y =', y
    print 'z =', z

f(10)
f(10, 20)
f(10, z=20)
f(10, z=20, y=30)
f(z=10, y=30, x=20)
# f(x=20, 30) # invalid syntax
# f(30, x=20) # multiple values for x

def f(x, y=1, z=2, **kw):
    print 'f(x, y=1, z=2, **kw)'.center(50, '=')
    print 'x =', x
    print 'y =', y
    print 'z =', z
    print 'kw =', kw


f(10)
f(10, 20)
f(10, abc=456, xyz=678)

# def f(**kw):
#   pass
# means the function can accept any number of KEYWORD arguments
#  -> packed into a dictionary

def f(x, y=1, z=2, *args, **kwargs):
    print 'f(x, y=1, z=2, *args, **kwargs)'.center(50, '=')
    print 'x=', x
    print 'y=', y
    print 'z=', z
    print 'args=', args
    print 'kwargs=', kwargs


f(10)
f(10, y='abc')
f(10, z=3)
f(10, 20, 30)
f(10, 20, 30, 40, 50, 60)
f(10, 20, 30, 40, 50, 60, a=10, b=20, c=30)

# Rule: * in a function DEFINITION
#       packs all additional POSITIONAL arguments into a TUPLE (order matters)
# Rule: ** in a function DEFINITION
#       packs all additional KEYWORD arguments into a DICT (names matter)

def g():
    return 1, 2, 3, 4, 5, 6

result = g()

def f(*args):
    print 'f(*args)'.center(50, '=')
    for a in args:
        print a

def h(a, b, c, x, y, z):
    print 'h(a, b, c, x, y, z)'.center(50, '=')
    print 'a=', a
    print 'b=', b
    print 'c=', c
    print 'x=', x
    print 'y=', y
    print 'z=', z
    
result = g()
f(*result)
h(*result)

args = {'a': 10, 'b': 20, 'c': 30, 'z': 40}

def f(a, b, c, z):
    print 'f(a, b, c, z)'.center(50, '=')
    print 'a =', a
    print 'b =', b
    print 'c =', c
    print 'z =', z

f(**args)
f(a=args['a'], b=args['b'], c=args['c'], z=args['z'])

# Rule: * in a function CALL
#      means UNPACK a SEQUENCE into POSITIONAL arguments
# Rule: ** in function CALL
#      means UNPACK a MAPPING into KEYWORD arguments

def f(a, b, c=None, *args, **kwargs):
    print 'f(a, b, c=None, *args, **kwargs)'.center(50, '=')
    print 'a =', a
    print 'b =', b
    print 'c =', c
    print 'args =', args
    print 'kwargs =', kwargs

# f(1)
f(1, 2)
f(1, c='abc', b='xyz')
f(*(1,2,3))
f(*(1,2,3,4,5,6,7,8))
f(**{'a': 10, 'b': 30, 'z': 50, 'w': 70})




# Rule: required arguments before optional arguments
# Rule: positional arguments before keyword arguments













    

























