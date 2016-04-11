import re

with open('notes/team_history.txt') as f:
    hist = f.read()

print hist

for mo in re.finditer(r'([0-9]+)/([0-9]+)/([0-9]+)', hist):
    month, day, year = [int(s) for s in mo.groups()]
    print 'The month is %s.  The day is %s and year is %s' % (month, day, year)

scores = [int(s) for s in re.findall(r'(\d+) point', hist)]
print 'Best score:', max(scores)
print 'Worst score:', min(scores)
print 'Cumulative:', sum(scores)
print 'Number games:', len(scores)
