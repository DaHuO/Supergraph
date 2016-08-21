#!/usr/bin/env python3

#from pprint import pprint

f = open("A-large.in")
#f = open("input.txt")
o = open("output.txt", "w")

t = int(f.readline())

for i in range(t):
    n = int(f.readline())

    if n == 0:
        o.write("Case #{}: INSOMNIA\n".format(i+1))
    else:
        mem = []
        x = 0
        c = 0
        while c!=10:
            x += n
            for d in str(x):
                if d not in mem:
                    mem.append(d)
                    c += 1
        o.write("Case #{}: {}\n".format(i+1, x))