# review.py

from __future__ import division # "pragma"

print 'Hello world!'
print "Hello world!"
print '''
Hellooooo...
World!
'''
print """
Hi!
How are you?
"""

print r'C:\\Users\travis\My Documents'

print u'I \N{heavy black heart} you! \N{LONG LEFTWARDS SQUIGGLE ARROW}'

print 'Hello', 'Krishnan'
name = 'Krishnan'
print 'Hello', name

point = -1, 0, 1

print 'Hello, %s, welcome to day %d!' % (name, 2)
print 'The point is at %d, %d, %d' % point
print 'The point is at %s' % (point,)

for i in range(5):
    print ' ' * i + 'Good morning!'
for i in range(4, -1, -1):
    print ' ' * i + 'Good morning!'


# numeric types:
int, float, complex, bool

# all Python integers are signed integers

print 2 ** 20000 # automatic promotion for integers

x = 0
x = x + 1
x += 1
# x++
++x

print 44 / 5  # "true division"
print 44 // 5 #  explicit "floor division"

#    mutable    immutable
#     list        str
#     dict        tuple
#     set

#   sequences   non-sequences
#    list           dict
#   tuple           set
#     str


empty_string = ''
empty_list   = []
empty_dict   = {}
empty_set    = set()
empty_tuple  = ()

some_list  = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
some_dict  = {0: 1, 1: 2, 2: 4, 4:16, 3:8, 5:32}
some_tuple = (1, 2, 4, 8, 16)
some_tuple = 1, 2, 4, 8, 16 # parens are optional
some_set   = {1, 2, 4, 8, 16}

some_list.append((10, 20))

list_of_tuples = [(0,1), (1,2), (2, 4), (3,8)]

xs = [1, 2, (), False, 'abc', 2+3j]
student = 'Krishnan', 'Ramamurthi', '917-283-2912', 12, 3.95

firstname, lastname, phone, age, gpa = student

points = [(1,2,3), (4,5,6), (-1,2,3)]
for x, y, z in points:
    print '@ x=', x, 'y=', y, 'z=', z


# d = {}
# d[key] = value

