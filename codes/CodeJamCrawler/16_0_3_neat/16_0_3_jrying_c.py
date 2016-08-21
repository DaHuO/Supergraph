import sys
import fileinput
import re

#fileio
fileName = 'C-large'
# fileName = 'C-small-attempt0'
# fileName = 'C-test'
input = fileName + ".in"
output = fileName + ".out"

###
with open(input) as fi, open(output, "w") as fo:
    base = 3
    prime = [2]
    while len(prime) < 1000:
        isp = True
        for p in prime:
            if p > base**0.5: break
            if base % p == 0:
                isp = False
                break
        if isp : prime.append(base)
        base += 2
    # print prime
    for line in fi.readlines()[1:]:
        print line
        N, J = map(int, line.split())
        result = 0
        ###
        j = {}
        for i in xrange(2**(N-1)+1, 2**N, 2):
            s = bin(i)[2:]
            d = []
            isj = True
            for b in range(2, 11):
                k = int(s, b)
                isd = False
                for p in prime:
                    if k % p == 0:
                        isd = True
                        d.append(str(p))
                        break
                if not isd:
                    isj = False
                    break
            if isj:
                j[i] = d
            if len(j) == J:
                break

        ###
        #normal
        fo.write("Case #1:\n")
        for x in j:
            fo.write(bin(x)[2:]+" "+" ".join(j[x])+'\n')
