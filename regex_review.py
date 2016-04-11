# regex_review.py

import re

'''
Basics
======
abcd               exact match of the string 'abcd'
a.cd               dot matches any character (except a newline)
                     DOTALL: allows the dot to match newlines
[aeiou]            matches anything inside the []
[A-Za-z0-9,]       matches anything within these ranges
                        [ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjijklmnopqrstuvwxyz0123456789,]
[^aeiou]           matches anything NOT in the group aeiou
                      ^ at the beginning of a []-set means set-complement
abc|def            matches either abc or def

Quantifiers (how many times)
============================

a*      zero or more          a{0,}
a+      one or more           a{1,}
a?      zero or one           a{0.1}
a{m,n}  between m and n times

Make quantifiers non-greedy:
a*?
a+?
a{m,n}?


Character Ranges
================

\s       [ \t\f\v\r\n]   any whitespace
\d       [0-9]           any digit
\w       [a-zA-Z0-9_]    any word character
            with .LOCALE:  [0-9_] | alphanumeric
            with .UNICODE: [0-9_] | alphanumeric
\S       [^ \t\f\v\r\n]  any NON-whitespace
\D       [^0-9]          any NON-digit
\W                       any NON-word character

Position
========

^      beginning of the string
$      the end of the string
\b     match on word boundary

match objects
=============
mo.start(), mo.end()      starting, ending index of the match
mo.span()                 (start, end) index as a tuple
mo.groups()               all the capture groups
mo.group(0)               entire string that matched
mo.group(x)               x>0, that specific matching group

`re` functions
==============
re.search(pattern, string)    ->   the first match (match object)
re.findall(pattern, string)   ->   find all the matches (as a list of strings)
re.finditer(pattern, string)  ->   find all the matches (as an iterable of match objects)

flags
=====
DOTALL       makes the dot character match all character (incl. newlines)
MULTILINE    allow matching beyond line endings (^$ mean beginning/end of string not line)
IGNORECASE   case insensitive
UNICODE      unicode compability
'''

text = 'take took truck fake fluke threat to make tale'
for mo in re.finditer('(t|f)(ake)', text):
    print mo.groups()

data = '''
 id = 2938123    start = 2014-02-23  # id = 232    start = 2016.01.09
 id = 292  \t   start = 2015/06/21
     id = 327    start = 20101014
'''

for line in data.splitlines():
    for mo in re.finditer('^\s*id = (\d{3,})\s+start = (\d{4}).?(\d{2}).?(\d{2})' , line):
        print int(mo.group(1)), int(mo.group(2)), int(mo.group(3)), int(mo.group(4))

text = '<a href="http://www.cisco.com">Cisco</a><a href="http://www.apple.com">Apple</a>'

print re.findall('<a href="(.+?)">.+?</a>', text)
