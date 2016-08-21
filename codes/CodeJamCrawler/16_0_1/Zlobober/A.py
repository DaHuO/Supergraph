#!/usr/bin/python

def solve(cs):
    n = int(raw_input())
    if n == 0:
        print "Case #{0}: INSOMNIA".format(cs)
        return 
    seen = set()
    cur = n
    it = 0
    while True:
        it += 1
        assert it <= 100
        seen |= set(str(cur))
        if len(seen) == 10:
            break
        cur += n
    print "Case #{0}: {1}".format(cs, cur) 

T = int(raw_input())
for i in range(T):
    solve(i + 1)
