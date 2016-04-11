# variables.py

# variables C vs variables in Python

x = 'This is a very long string in Python.'
print x

y = x
z = 'This is a very long string in Python.'

print x == y # checking for equality (equivalence)
print x == z
print x is y # checking for identity
print x is z

x = [1,2,3]
y = x
z = [1,2,3]

# if x == y           (does NOT imply)      x is y
# if id(x) == id(y)   (always implies)      x is y
# if x is y           (usually implies)     x == y
