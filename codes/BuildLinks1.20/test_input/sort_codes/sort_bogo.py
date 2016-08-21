import fileinput
from random import shuffle
from timer import Timer

l = []
for i in fileinput.input():
    l.append(int(i))

def sort_bogo(l):
    while not all(l[i-1] <= l[i] for i in xrange(1, len(l))):
        shuffle(l)
    return l

with Timer() as t:
    l = sort_bogo(l)

print l
print('List length: %i' % len(l))
print('Sort time: %.05fs' % t.interval)