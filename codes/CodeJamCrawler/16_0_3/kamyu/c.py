from math import sqrt

def coin_jam():
    N, J = map(int, raw_input().strip().split())
    start = 1 << ((N / 2) - 2)
    for i in xrange(start, start + J):
        binary = bin(i)[2:] + "1"
        binary *= 2
        print " ".join(map(str, [binary] + [pow(i, N / 2) +  1 for i in xrange(2, 11)]))
    
for case in xrange(input()):
    print 'Case #%d:' % (case+1)
    coin_jam()
