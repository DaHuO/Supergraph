#!/usr/bin/python

import sys

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def checkCornerCases(N):
    if len(str(N)) == 1 and N == 0:
        return True
    #elif len(str(N)) == 2 and N in []:
    #    return True
    #elif len(str(N)) == 3 and N in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
    #    return True

def A(n, N):
    if checkCornerCases(N):
        sys.stdout.write("Case #%d: %s\n" %(n, "INSOMNIA"))
        return

    m = 1
    digits = []
    NN = N
    while(len(digits) < 10):
        #print(NN)
        strNN = str(NN)
        l = len(strNN)
        for i in range(0, l):
            d = strNN[i: i+1]
            if d not in digits:
                digits.append(d)
            if len(digits) == 10:
                #print(digits)
                sys.stdout.write("Case #%d: %d\n" %(n, NN))
                break
        m = m + 1
        NN = N * m


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        T = int(f.readline())
        #print(T)
        n = 0
        while T > 0:
            N = int(f.readline())
            n = n + 1
            A(n, N)
            T = T - 1    

