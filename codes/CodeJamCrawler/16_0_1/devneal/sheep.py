#!/usr/bin/python

T = input()

for i in range(T):
    N = input()
    if N == 0:
        print "Case #{}: INSOMNIA".format(i+1)
        continue

    seen = set()

    mult = 1
    val = 0
    while len(seen) < 10:
        val = N*mult
        for ch in str(val):
            seen.add(ch)
        mult += 1
    print "Case #{}: {}".format(i+1,val)
