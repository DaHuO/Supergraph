#
# Google Code Jam 2016
# Roaund 0: B. Revenge of the Pancakes
# submission by EnTerr
#

'''

Input

The first line of the input gives the number of test cases, T. T test
cases follow. Each consists of one line with a string S, each character
of which is either + (which represents a pancake that is initially happy
side up) or - (which represents a pancake that is initially blank side
up). The string, when read left to right, represents the stack when
viewed from top to bottom.

Output

For each test case, output one line containing Case #x: y, where x is
the test case number (starting from 1) and y is the minimum number of
times you will need to execute the maneuver to get all the pancakes
happy side up.

Limits: 1 <= T <= 100.
Small dataset: 1 <= length of S <= 10.
Large dataset: 1 <= length of S <= 100.

Input 
5
-
-+
+-
+++
--+-

Output 
Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3

'''


import sys
from time import clock


f = open(sys.argv[1])
def input(): return f.readline().strip();

       
def count_flips(p_stack):
    num_inv = 0
    prev = '+'
    # go backwards, from the bottom
    for p in p_stack[::-1]:   
        # count number of inversions
        if p <> prev: 
            num_inv += 1
        prev = p
    return num_inv
	

#clk = clock()

for caseNo in xrange(1, int(input())+1):
#    print >>sys.stderr, caseNo
    p_stack = input()
    print 'Case #%d:' % caseNo, count_flips(p_stack)
    
#print >>sys.stderr, 'time= %.1f seconds' % (clock()-clk )

