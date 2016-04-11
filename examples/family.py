# family.py

import json

def as_str(family):
    body = []
    line_template = '%-15s (%d-%d) %s'
    for firstname, middle, gender, month, day, interests in family:
        line = line_template % (firstname, month, day, ', '.join(interests))
        body.append(line)
    return '\n'.join(body)

html_template = '''
<html>
    <head>
        <title>Our Family</title>
    </head>
    <body>
    <h1>Our family:</h1>
        <ul>
%s
        </ul>
    </body>
</html>'''
member_template = '''
    <li><b>%s</b> (%d-%d): %s</li>
'''

def as_html(family):
    body = []
    for first, middle, gender, month, day, interests in family:
        body.append(member_template % (first, month, day, ', '.join(interests)))
    return html_template % ''.join(body)

if __name__ == '__main__':
    family = [
        ('Homer', 'J', 'male',   4, 12, ('sports', 'boats')),
        ('Marge',  '', 'female', 5, 21, ('computers', 'planes')),
        ('Bart',   '', 'male',   9, 13, ('cars', 'planes', 'boats')),
        ('Lisa',   '', 'female', 6, 9,  ()),
    ]

    print as_html(family)
    print as_str(family)
    print json.dumps(family, indent=1)
