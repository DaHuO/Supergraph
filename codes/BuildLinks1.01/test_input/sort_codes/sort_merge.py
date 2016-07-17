import fileinput
from random import shuffle
from timer import Timer

l = []
for i in fileinput.input():
    l.append(int(i))

def merge(a, b):
    l = []
    while len(a) > 0 or len(b) > 0:
        if len(a) > 0 and len(b) > 0:
            if a[0] <= b[0]:
                l.append(a.pop(0))
            else: # b[0] < a[0]
                l.append(b.pop(0))
        elif len(a) > 0:
            l.append(a.pop(0))
        else: # len(b) > 0
            l.append(b.pop(0))
    return l

def sort_merge(l):
    if len(l) <= 1:
        return l
    middle = int(len(l)/2)
    left = []
    right = []
    for x in xrange(0, middle):
        left.append(l[x])
    for x in xrange(middle, len(l)):
        right.append(l[x])
    
    left = sort_merge(left)
    right = sort_merge(right)
    return merge(left, right)

with Timer() as t:
    l = sort_merge(l)

print l
print('List length: %i' % len(l))
print('Sort time: %.05fs' % t.interval)