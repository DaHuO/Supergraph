#!/usr/local/bin python

t = int(raw_input())
ns = []

for i in range(t):
    ns.append(int(raw_input()))

for i in range(len(ns)):
    known_numbers = []

    j = 0
    while True:
        j += 1
        p = str(j * ns[i])
        ret = 0
        if p == '0':
            ret == 1
            p = "INSOMNIA"
            break
        for c in p:
            if int(c) not in known_numbers:
                known_numbers.append(int(c))
                known_numbers.sort()
                if known_numbers == [0,1,2,3,4,5,6,7,8,9]:
                    ret = 1
                    break
            if ret == 1: break
        if ret == 1: break
    print 'Case #{0}: {1}'.format(i+1, p)

