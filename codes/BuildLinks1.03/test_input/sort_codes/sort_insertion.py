import fileinput
from timer import Timer

l = []
for i in fileinput.input():
    l.append(int(i))

def insertion(l):
    for i in xrange(1, len(l)):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j = j-1
    return l

def insertion_n_mem(l):
    l_sorted = []
    for i in l:
        for x in xrange(len(l)):
            try:
                if i < l_sorted[x]:
                    l_sorted.insert(x, i)
                    break
            except IndexError:
                l_sorted.append(i)
                break
    l = l_sorted

in_place = True
with Timer() as t:
    if in_place:
        l = insertion(l)
    else:
        l = insertion_n_mem(l)

print l
print('List length: %i' % len(l))
print('Sort time: %.05fs' % t.interval)