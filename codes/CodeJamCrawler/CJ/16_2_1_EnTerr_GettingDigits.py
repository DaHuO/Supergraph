#
# Google Code Jam 2016
# Roaund 1A: C. BFFs
# submission by EnTerr
#

'''
Input

The first line of the input gives the number of test cases, T. T test
cases follow. Each consists of one line with a string S of uppercase
English letters.

Output

For each test case, output one line containing Case #x: y, where x is
the test case number (starting from 1) and y is a string of digits: the
phone number.

Limits   1 <= T <= 100. A unique answer is guaranteed to exist. 
Small dataset 3 <= length of S <= 20.
Large dataset 3 <= length of S <= 2000.

Input 

4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER
 	
Output 
 
Case #1: 012
Case #2: 2468
Case #3: 114
Case #4: 3

'''


import sys
from time import clock
from collections import defaultdict

f = open(sys.argv[1])
def input(): return f.readline().strip();

       
def get_digits(s):
    '''
    given string, figure out digits, return str in increasing order
    '''
    d = defaultdict(int)
    for ch in s:
        d[ch] += 1
    res = [ ]
    # order is important, first letter determined the digit
    key = [('ZERO', 0), ('WTO', 2), ('GEIHT', 8), ('THREE', 3), ('RFOU', 4), ('ONE', 1), ('FIVE', 5), ('XSI', 6), ('INNE', 9), ('SEVEN', 7)]
    for ltrs, dig in key:
        while d[ltrs[0]] > 0:
            res.append(dig)
            for ch in ltrs:
                d[ch] -= 1
    return ''.join(str(i) for i in sorted(res))


#clk = clock()

for caseNo in xrange(1, int(input())+1):
    #print >>sys.stderr, caseNo
    print 'Case #%d:' % caseNo, get_digits(input())
    
#print >>sys.stderr, 'time= %.1f seconds' % (clock()-clk )

