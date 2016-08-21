#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')
    
T = int(input.readline())

def fake(title, titles):
    lst = titles.difference([title])
    return title[0] in [x[0] for x in lst] and title[1] in [x[1] for x in lst]

d = {}

def count(titles):
    if not titles:
        return 0
    if titles in d:
        return d[titles]
    lst = []
    for t in titles:
        rest = titles.difference([t])
        if fake(t, rest):
            n = 1
        else:
            n = 0
        n += count(rest)
        lst.append(n)
    d[titles] = max(lst)
#    print d[titles], titles
    return d[titles]
        
def solve():
    N = int(input.readline())
    titles = []
    for i in range(N):
        titles.append(tuple(input.readline().strip().split(' ')))
    return count(frozenset(titles))

for t in range(T):
    print t
    print >> output, 'Case #%s: %s' % (t+1,solve())

