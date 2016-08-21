#!/usr/bin/python

T = int(input())
results = []
for case in range(1,T+1):
    N = int(input())
    k = N
    if N != 0:
        unique_set = set(str(N))
        while (len(unique_set) < 10):
            N += k
            unique_set |= set(str(N))
        results.append((str(case),str(N)))
    else:
        results.append((str(case), "INSOMNIA"))

for (case,i) in results:
    print("Case #%s: %s" % (case,i))
