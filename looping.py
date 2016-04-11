# looping.py

colors = 'red blue yellow       \t\n green black blue'

print '''task 1: loop over the colors and print them out capitalized

    Red
    Blue
    Yellow
    Green
    Black
    Blue

'''

for color in colors.split():
    print color.capitalize()


print '''task 2: loop over the colors and print the color in ALL CAPS and the position in the list

    0 RED
    1 BLUE
    2 YELLOW
    3 GREEN
    4 BLACK
    5 BLUE
'''

for idx, color in enumerate(colors.split()):
    print idx, color.upper()

colors = 'red blue yellow yellow green turqoise red chartreuse purple'

print '''task 3: loop over the unique colors (in alphabetical order'''

for color in sorted(set(colors.split())):
    print color

colors = 'red blue yellow yellow green turqoise red chartreuse purple'

print '''task 4: print the colors and the number of times they appear
    red 2
    blue 1
    yellow 2
    green 1
    turqoise 1
    chartreuse 1
    purple 1
'''

from collections import Counter
hist = Counter(colors.split())

for color, count in sorted(hist.items()):
    print color, count

animals = 'tiger lion bear monkey rabbit hippopotamus rhino ox'

print 'task 5: loop over the animals in the zoo in alphabetical order'

for animal in sorted(animals.split()):
    print animal


print 'task 5a: loop over the animals in the zoo in order of longest to shortest name'

for animal in sorted(animals.split(), key=len, reverse=True):
    print animal


animals = 'tiger lion     bear  monkey rabbit hippopotamus rhino   ox'
colors  = 'orange yellow  black brown  grey    pink         grey   maroon'
sizes   = 'medium big     big   small  tiny    huge         huge   big'

print '''task 6: associate each color with the corresponding animal and print them out

    tiger orange
    lion  yellow
    bear  black
    monkey brown
    rabbit grey
    ...
'''

for animal, color, size in zip(animals.split(), colors.split(), sizes.split()):
    print 'I saw a %s, %s %s at the zoo today!' % (size, color, animal)

print '''task 6a: create a mapping of each animal to its usual color'''

animal_colors = {}
for animal, color in zip(animals.split(), colors.split()):
    animal_colors[animal] = color


# comprehension syntax
animal_colors = {animal:color for animal, color in zip(animals.split(), colors.split())}

animal_colors = dict(zip(animals.split(), colors.split()))

en_zh = {
    'one': 'yi',
    'two': 'er',
    'three': 'san',
    'four': 'si',
    'five': 'wu'
}

zh_en = {}
for en_word, zh_word in en_zh.items():
    zh_en[zh_word] = en_word

zh_en = {v:k for k,v in en_zh.items()}

animals = 'zebra;owl;giraffe;monkey;lion;tiger;gorilla;hippopotamus'

print '''task 7: print the animal names in order of the number of vowels in their names'''

def count_vowels(word):
    return sum([ c in 'aeiou'   for c in word  ])

for animal in sorted(animals.split(';'), key=count_vowels):
    print animal

