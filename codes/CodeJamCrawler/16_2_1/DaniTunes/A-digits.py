#!/bin/env python

# google code jam 2016 round 1B problem A
# Daniel Scharstein

import sys
d = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
n = {}

for i, w in enumerate(d):
    n[w] = i

a = {}
for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    #print x,
    for w in d:
	if x in w:
	    #print w,
	    if x in a:
		a[x].append(w)
	    else:
		a[x] = [w]
    #print

#for k in a:
#    print k, a[k]

c = []
done = False
while not done:
    done = True
    for k in a:
	#print k, a[k]
	if len(a[k]) == 1:
	    if k not in c:
		c.append(k)
	    w = a[k][0]
	    for j in a:
		if j != k and w in a[j]:
		    a[j].remove(w)
		    done = False
#print
#for k in c:
#    print k, a[k]

def contained(a, b):
    for c in a:
	if c not in b:
	    return False
    return True

def remove(a, b):
    for c in a:
	b.remove(c)
	
def solve(s):
    b = list(s)
    r = []
    for k in c:
	w = a[k][0]
	while contained(w, b):
	    remove(w, b)
	    r.append(str(n[w]))
    r.sort()
    return "".join(r) 

tests = int(raw_input())
for k in range(tests):
    s = raw_input()
    x = solve(s)
    print "Case #%d: %s" % (k+1, x)
