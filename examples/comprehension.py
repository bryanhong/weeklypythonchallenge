# comprehension.py

from __future__ import division # 'pragma' 

xs = [1, 2, 3, 50, -10, -5000, 255]

print 'task 1: calculates the average of xs'

def average(seq):
    return sum(seq) / len(seq)

print average(xs)

print 'task 2: calculate the minimum value in xs = -5000'
print 'task 3: calculate the maximum value in xs = 50'

print min(xs)
print max(xs)

print 'task 4: calculate the min magnitude (abs val) in xs = 1'
print 'task 5: calculate the max magnitude (abs val) in xs = -5000'

print min(xs, key=abs)
print max(xs, key=abs)

print 'task 6: calculate the number in xs which has the most 1s in its binary representation'

def num_ones(x):
    return bin(x).count('1')

print max(xs, key=num_ones)

print 'task 7: calculate the variance & standard deviation of xs'

import math

def stddev(seq):
    return math.sqrt(var(seq))

def var(seq):
    mean = average(seq)
    total = 0
    for x in seq:
        total += (x - mean) ** 2
    return total / len(seq)

def var(seq):
    mean = average(seq)
    squares = []
    for x in seq:
        squares.append((x - mean) **2)
    return average(squares)

# list comprehension

ys = [1, 3, 6, 10, 15, 17, 20]

xs = [ y ** 2 for y in ys if y % 2 == 1 ]

xs = [    y ** 3             for y                  in ys        if y > 5    ]
#         expression         loop variable         iterable      filter/predicate 

def variance(xs):
    mean = average(xs)
    return average([ (x - mean)**2 for x in xs ])

xs = {y - 2 for y in ys if y > 14}

xs = {y: y-2 for y in ys if y in {1,6,10,17,24}}


fruits = {'apple', 'banana', 'orange', 'grape', 'watermelon'}
vowel_fruits = {len(fruit) for fruit in fruits if fruit.startswith(('a', 'e', 'i', 'o', 'u'))}

     #    snacks?  open-plan?
buildings = [
    ('i',  False, True),
    ('32', True,  True),
    ('18', True,  True),
    ('m',  False, False),
]

parking = {
    'i': True,
    '32': False,
    '18': False,
    'm': True
}

best_offices = {}
for name, snacks, open_plan in buildings:
    if snacks:
        best_offices[name] = parking[name]
print best_offices

Index
print {name    for name, snacks, open_plan in buildings       if snacks     }

        

