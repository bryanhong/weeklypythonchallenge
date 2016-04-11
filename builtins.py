# builtins.py

all_builtins = set(dir(__builtins__))
ignore = {'license', 'copyright', 'apply', 'basestring', 'credits', 'coerce', 'cmp'}
all_builtins -= ignore
types = {'int', 'long', 'str', 'dict', 'list', 'tuple', 'bool', 'set', 'complex', 'file', 'float', 'frozenset', 'object', 'slice', 'unicode', 'Ellipses'}
all_builtins -= types
errors = {x for x in all_builtins if 'Error' in x or 'Warning' in x or 'Interrupt' in x or 'Exit' in x}
all_builtins -= errors
special = {x for x in all_builtins if '__' in x}
all_builtins -= special

intermediate = {'property', 'staticmethod', 'buffer', 'bytes', 'callable', 'classmethod', 'execfile', 'eval', 'getattr', 'hasattr', 'setattr', 'delatt'}
advanced = {'memoryview', 'bytearray', 'compile', 'intern'}

all_builtins -= intermediate
all_builtins -= advanced

print all_builtins

print abs(-10)

# False-ish
# - empty
# - zero
# - None

print any([True, False, [], 0, 'abc'])
print all([True, [[]], 0.1, 'abc'])

print chr(97), ord('a'), chr(ord('x')), ord(chr(97))

print oct(31) == 25

globals()
locals()
vars()

print isinstance([], list)
print isinstance(10, float)
print isinstance(True, int)

print issubclass(bool, int)
print issubclass(int, object)

# map
# filter

def f(x):
    return x * 10
print map(f, [1,2,3,4])
print [x * 10 for x in [1,2,3,4]]

def f(x):
    return x < 10
print filter(f, [1,2,10,20])
print [x for x in [1,2,10,20] if x < 10]

# reversed
# sorted

xs = {'in-n-out', 'five guys', 'shake shack', 'carls jr', 'jack in the box', 'whataburger', 'chick-fil-a'}

reviews = {'in-n-out':        'a',
           'five guys':       'b',
           'shake shack':     'b',
           'carls jr':        'd',
           'jack in the box': 'c',
           'whataburger':     'b',
           'chick-fil-a':     'A',
           'subway':          'f'}

for restaurant in sorted(xs):
    print restaurant

for restaurant in reversed(sorted(xs)):
    print restaurant

for restaurant in sorted(xs, reverse=True):
    print restaurant

print '=' * 50
for restaurant in sorted(reviews, key=reviews.get):
    print restaurant

# enumerate
# zip

for idx, restaurant in enumerate(xs, start=2):
    print idx, restaurant

restaurants = ['chick-fil-a',   "wendy's",       'in-n-out',      "carl's jr"                                     , 'taco bell',    "mcdonald's"]
dishes      = ['spicy chicken', 'spicy chicken', 'double double', "you're too old to still be eating at carl's jr", "doesn't matter; everything's the same"]

print '=' * 50
for restaurant, dish in zip(restaurants, dishes):
    print restaurant, dish

family = [
    ('Homer', 'J'),
    ('Marge',  'N/A'),
    ('Lisa',   'M'),
    ('Bart',   None),
    ('Maggie',  ''),
]

have_middle_name = [first for first, middle in family if middle and middle != 'N/A']

# xrange

d = {'uno': 'one', 'dos': 'two', 'tres': 'three'}
ks = d.viewkeys()
d['quatro'] = 'four'
d['cinco']  = 'five'
for k in ks:
    print k

for x in xrange(1000000):
    print x




