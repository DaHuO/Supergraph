import sys, numpy as np

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return -1
    if not n & 1: 
        return 2
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return x
    return -1

input = [x.strip().split() for x in sys.stdin.readlines()][1:]

for case, ip in enumerate(input):
    print 'Case #'+str(case+1)+':'
    N = int(ip[0])
    J = int(ip[1])
    val = ['0' for _ in range(N)]
    val[0] = '1'
    val[-1] = '1'
    j = 0
    while j<J:
        flag = False
        divlist = []
        for base in range(2,11):
            n = int(''.join(val), base)
            divisor  = isprime(n)
            if divisor==-1:
                flag = True
                break
            else:
                #print ''.join(val), n, divisor
                divlist.append(divisor)
        if not flag:
            print ''.join(val),
            for d in divlist:
                print d,
            print
            j += 1

        candidate = list(bin(int(''.join(val[1:-1]),2)+1))[2:] # next candidate
        if(len(candidate)>(N-2)):
            break
        val = ['1'] + ['0' for _ in range(N-2-len(candidate))] + candidate + ['1']
