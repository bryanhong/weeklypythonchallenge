# objects.py

def heading(text):
    text = text.upper()
    text = text.center(len(text) + 4, ' ')
    text = text.center(80, '=')
    return text

# list
# tuples
# dict
# set
# function

print heading('list')

empty_list = []
fruits = ['orange', 'banana', 'strawberry', 'apple', 'blueberry', 'grapes']

for fruit in fruits:
    print 'I like %ss' % fruit

print 'I only like %ss' % fruits[0]
print 'I only like %ss' % fruits[-1]

print 'I like these fruits: %s' % ', '.join(fruits[1:-2])

fruits.append('mango')
print fruits
fruits += ['tomato']
print fruits

fruits.insert(1, 'kiwi')
print fruits

fruits = ['dragonfruit'] + fruits
fruits.insert(0, 'papaya')
print fruits

print 'I like at least %d fruits' % len(fruits)

fruits.append('apple')
fruits.append('apple')
print fruits
print fruits.count('apple')

fruits.reverse()
print fruits

fruits.sort()
print fruits

veggies = ['corn', 'carrots', 'beets']
fruits.extend(veggies)
print fruits

fruits = fruits[:-2]
print fruits

fruits.remove('dragonfruit')
fruits.remove('apple')
print fruits

while 'apple' in fruits:
    fruits.remove('apple')
print fruits

fruits = []
fruits.append('kiwi')
fruits.append('watermelon')
fruits.append('grapes')

print fruits.pop()
print fruits.pop()
print fruits.pop()

fruits = ['apple', 'orange', 'pear']
fruits[0] = 'watermelon'
print fruits

# lists are mutable
# lists are sequences (they are indexed)
#           sequences (they -human- ordered)
# list can be hetergeneous (different types of contents, but not very useful)

xs = ['a', 10, []]

print heading('tuple')

x = (2, 3, 4)
x = 2, 3, 4 # the parens are optional
empty_tuple = ()

# tuple are sequences (they are indexed & human ordered)
# tuple is immutable
# tuple can be heterogeneous (frequently useful)

some_list = [1, 2, 3]
some_list.append(20)
some_list[0] = 10

some_tuple = 1, 2, 3
# some_tuple[0] = 10

point = 10, 20, 30
print point[0], point[1], point[2]
print point[:2]

x = 2, 3
y = 4, 5
print x + y

# both tuples and lists are "heterogeneous"

# tuples are good represention for records (a struct)
student = 'Chandler', 'Frahm', 25, '782-493-2918', 3.4
students = [
    ('Chandler', 'Frahm', 25, '782-493-2918', 3.4),
    ('Michael', 'Litwicki', 32, '872-493-2918', 3.9)
]

for student in students:
    print student[-2]

point = 1, -2, 1
x, y, z = point # unpacking
print 'the point is at', 'x=', x, 'y=', y, 'z=', z

for lastname, firstname, age, phone, gpa in students:
    print firstname, 'has a gpa of', gpa

from collections import namedtuple
Person = namedtuple('Person', ['firstname', 'lastname', 'age', 'phone', 'gpa'])
students = [
    Person('Chandler', 'Frahm', 25, '782-493-2918', 3.4),
    Person('Michael', 'Litwicki', 32, '872-493-2918', 3.9)
]

for student in students:
    print student.firstname, 'has a gpa of', student.gpa


x, y = 10, 20

w = 30
z = 40

w, z = z, w
print w, z

a, b, c = 10, 20, 30
a, b, c = c, a, b + c

print heading('dict')

# key-value pair/store
# hash
# map
# 2d list
# associative array
# many-to-one/many mapping
    
en_hi = {
    'blue':  'nila',
    'red':    'lal',
    'yellow': 'pila',

    # values do not have to be unique
    # there is NO restriction on the values of a dictionary
    'yesterday': 'kal',
    'tomorrow':  'kal',

    # keys must be unique
    # the keys of a dictionary must be immutable
    'white': 'safed',
    'white': 'schwed'
}

print 'To say "blue" in Hindi, you say:', en_hi['blue']
print 'To say "white" in Hindi, you say:', en_hi['white']

print 'purple' in en_hi
print 'white' in en_hi

# dictionaries are mutable
en_hi['green'] = 'hara'
en_hi['white'] = 'schwet'
del en_hi['red']
print en_hi

# Python dictionaries iterate over their keys
for word in en_hi:
    print word

for word in en_hi:
    print word

for word in en_hi:
    print word, 'is said', en_hi[word]

for hindi_word in en_hi.values():
    print hindi_word

for en_word, hi_word in en_hi.items():
    print en_word, '-->', hi_word

print heading('set')

empty_dictionary = {}
some_dictionary = {1:2, 2:4, 3:9, 4:16}

some_set = {1, 2, 4, 8, 16}
empty_set = set()

jennifer_foods = {'pizza', 'french', 'indian'}
huynh_foods = {'italian', 'vietnamese', 'indian'}
raj_foods = {'burgers', 'mexican', 'italian'}

print 'burgers' in raj_foods

# sets are also machine ordered
for food in jennifer_foods:
    print food

print jennifer_foods & huynh_foods # set intersection
print raj_foods | jennifer_foods   # set union
print len(jennifer_foods | huynh_foods)
print 'korean' in jennifer_foods
print 'indian' in huynh_foods

print jennifer_foods | huynh_foods | raj_foods

print raj_foods - huynh_foods # set difference
print raj_foods ^ huynh_foods # set symmetric difference

# sets are mutable
huynh_foods.add('chinese')
raj_foods.remove('italian')

print huynh_foods
print raj_foods


#                     mutable        immutable
# sequences            list           tuple, str
# not sequences      dict, set       (frozenset)
#

print heading('functions')

def repeat(element, times=3, before='<', after='>'):
    return before + (element * times) + after

print repeat('abc', 5)
print repeat('abc')
print repeat('abc', 10, '(', ')')
print repeat('xyz', before='(')

def func(x):
    return x * 2

print func(10)
print func('abc')
print func([1,2,3])

def none_return(x):
    pass # no-op

def none_return(x):
    return

def none_return(x):
    return None

