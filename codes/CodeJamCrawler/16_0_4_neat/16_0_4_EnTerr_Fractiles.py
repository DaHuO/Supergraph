#
# Google Code Jam 2016
# Roaund 0: D. Fractiles
# submission by EnTerr
#

'''

Input

The first line of the input gives the number of test cases, T. T test
cases follow. Each consists of one line with three integers: K, C, and
S.


Limits

1 <= T <= 100.
1 <= K <= 100.
1 <= C <= 100.
KC <= 10^18.

Small dataset:  S = K.
Large dataset:  1 <= S <= K.

Sample

*** Input 
5
2 3 2
1 1 1
2 1 1
2 1 2
3 2 3

*** Output 
Case #1: 2
Case #2: 1
Case #3: IMPOSSIBLE
Case #4: 1 2
Case #5: 2 6

'''


import sys
from time import clock


f = open(sys.argv[1])
def input(): return f.readline().strip();

       
def fractiles(k, c, s):
    if k > s: return 'IMPOSSIBLE'
    return ' '.join(str(i) for i in range(1, k+1))


#clk = clock()

for caseNo in xrange(1, int(input())+1):
#    print >>sys.stderr, caseNo
    K, C, S = map(int, input().split())
    print 'Case #%d:' % caseNo, fractiles(K, C, S)
    
#print >>sys.stderr, 'time= %.1f seconds' % (clock()-clk )

