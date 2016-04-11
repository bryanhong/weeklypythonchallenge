# strings.py

x = 'superman'
x = "clark kent"

# there is not difference ' and " in Python

print "Double quotes let us include 'single quotes' easily."
print '"Single quotes", I say authoritatively, "Are useful the other way around!"'

x = 'c'
print isinstance(x, str)

print '''
A mosquito did cry out in pain,
"A scientist's rotting my brain!"
The cause of his sorrow,
Was para-dichloro,
Diphenyl-tricholoroethane (DDT)
'''

print """
The mighty Thor,
He rode to war,
Upon his fine white filly.
"I'm Thor!" he cried;
The horse replied:
"Then wear a thaddle thilly!"
"""

print '\tThis is shifted over a bit\n'

print r'C:\\Users\travis\My Documents'

print u"Let's go build a \N{snowman} together!"
x = u'Python says, "I \N{heavy black heart} you!"'
print x

x = 'Hello'
y = 'world'

print x + ' ' + y
print (x + ' ' + y + ' ') * 5

msg = 'python loves YOU & hopes you love it, too!'

# "casers": things which change the case of a string
print msg.upper()
print msg.lower()
print msg.title() # usually not what you want
print msg.capitalize()

# "aligners": things which align a string
print msg.rjust(50)
print msg.ljust(50, '-')
print msg.center(80, '=')
print msg.center(50, '=').center(80, '+')


msg = '      This has a lot of       whitespace.      '

# "trimmers" ("strippers"/"chompers"): things which remove whitespace from a string
print msg.lstrip()
print msg.rstrip()
print msg.strip()

# "predicates": answer questions about strings

filename = 'snowman.jpeg'

print filename.startswith('snowman')
print filename.endswith('.jpeg')
print filename.islower()
print filename.isupper()
print filename.isspace()
print filename.isdigit()

print 'man' in filename

msg = "This is a silly string, but it's not 'silly-string'!"

for c in msg:
    print c

print '=' * 50
print msg[0]
print msg[-1]

# open-close interval
#   [start, stop)

# slice syntax
#   msg[start:stop:step]
#   msg[start:]
#   msg[:stop]
#   msg[start:stop]
#   msg[::step]

msg = 'Python loves you!'

print msg[:6]
print msg[-4:]
print msg[-4:-1]
print msg[::-1]


def count_excl_whitespace(string):
    r'count the characters in the string not include whitespace [\t\n\r\f\v ]'
    count = 0
    for c in string:
        count += not c.isspace()
    return count

def count_excl_whitespace(string):
    return len(string) - string.count(' ') - string.count('\t') - string.count('\n') # ...

msg = 'This is a t    est \t string \n'

print '=' * 80
print 'The length of the string without whitespace is:'
print count_excl_whitespace(msg)

path = '/usr/bin/python'
directory = path.split('/')[:-1]
print '/'.join(directory)

s = 'A sentence           is         this.'
print s.split()

sentence = "Python is a great language to use at companies like cisco or facebook!"
words = sentence.split()
words[-1] = words[-1].capitalize()
words[-3] = words[-3].capitalize()
print ' '.join(words)


