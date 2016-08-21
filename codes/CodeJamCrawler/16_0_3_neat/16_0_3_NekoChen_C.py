import sys

from itertools import combinations
from operator import itemgetter

def isComposite( x, base, guess ):
    x = int(x, base)
    return 0 == (x % guess)

def gen(N):
    N-=2
    for i in combinations( range(N/2), N/4 ):
        x, z = ['0']*(N/2), ['0']*N
        for p in i: x[p] = '1'
        z[0::2] = x
        for j in combinations( range(N/2), N/4 ):
            y = ['0']*(N/2)
            for p in j: y[p] = '1'
            z[1::2] = y
            yield "1" + "".join(z) + "1"

#g = gen(16)
#g.next()            

def isComposite( x, base, guess ):
    x = int(x, base)
    return 0 == (x % guess), x/guess

def test( s ):
    return [ isComposite(s,i,i+1) for i in range(2,11) ]

def solve( N, J ):
    generator = gen(N)
    for i in range(J):
        x = generator.next()
        print "{0} 3 4 5 6 7 8 9 10 11".format(x)

def main():
    f = open( sys.argv[1] )
    #f = sys.stdin
    T = int(f.next())
    for case in range(1,T+1):
        N, J = map(int, f.next().strip().split())
        print "Case #{0}:".format(case)
        solve( N,J )

if __name__ == "__main__":
    main()
