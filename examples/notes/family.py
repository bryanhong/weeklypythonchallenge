'Goal:  Learn patterns for output templating'

with open('notes/family_template.txt') as f:
    family_template = f.read()

with open('notes/member_template.txt') as f:
    member_template = f.read()

def show_family_html(lastname, first_names):
    'Display family members in an HTML format'
    members = []
    for name in first_names:
        member = member_template % name.title()
        members.append(member)
    print family_template % (lastname.title(), lastname.title(), ''.join(members))

def show_family(lastname, first_names):
    'Display family members in a nice tabular format'
    print 'The %s Family' % lastname.title()
    print '=' * (11 + len(lastname))
    for name in first_names:
        print '* %s' % name.title()
    print

if __name__ == '__main__':
    show_family_html(lastname='simpsons', first_names=['homer', 'marge', 'bart', 'lisa', 'maggie'])
