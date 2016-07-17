import fileinput
from timer import Timer

l = []
for i in fileinput.input():
    l.append(int(i))

def sort_bubble(l):
    n = len(l)
    while n > 0:
        nlast = 0
        for i in xrange(1, n):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
                nlast = i
        n = nlast
    return l

with Timer() as t:
    l = sort_bubble(l)

print l
print('List length: %i' % len(l))
print('Sort time: %.05fs' % t.interval)