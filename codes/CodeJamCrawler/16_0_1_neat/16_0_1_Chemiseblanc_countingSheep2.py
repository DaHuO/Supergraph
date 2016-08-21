#Google Codejam 2016 Problem 1
#Matthew Gibson @chemiseblanc mgibs029@uottawa.ca

import sys

data = sys.stdin.readlines()

outfile = open("output.txt",'w')

for i in range(len(data)):
    data[i] = int(data[i])

for i in range(1,data[0]+1):

    if data[i] != 0:
        digits = [0] * 10
        count = 0
        N = 0
        while digits != [1]*10:
            N += data[i]
            n = str(N)
            for j in range(len(n)):
                k = int(n[j])
                digits[k] = 1

        outfile.write("Case #%d: %d\n" % (i,N))
    else:
        outfile.write("Case #%d: INSOMNIA\n" % i)


