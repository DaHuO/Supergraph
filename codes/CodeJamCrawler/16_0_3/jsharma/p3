#!/c/Python27/python

import sys
import itertools

def isprime(n):
    for i in range(2, int(n ** .5)):
        if n % i == 0:
            return i

def calc(n, j):
    jcss = [] 
    jcsc = 0
    for jc in itertools.product(range(2), repeat = n - 2):
        jcs = '1' +  ''.join((str(d) for d in jc)) + '1'
        jcds = []
        for b in range(2,11): 
            jcb = int(jcs, b)
            jcd = isprime(jcb)
            if jcd:
                jcds.append(jcd)
            else:
                break
        else:
            jcss.append((jcs, jcds))
            jcsc += 1
            print >> sys.stderr, jcsc
            sys.stderr.flush()
            if len(jcss) == j:
                break
    return jcss 

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        N, J = (int(v) for v in sys.stdin.readline().split())
        print 'Case #%d:' % (i + 1)
        sys.stdout.flush()
        for jc in calc(N, J):
            print jc[0], ' '.join((str(n) for n in jc[1])) 

if __name__ == '__main__':
    main()
