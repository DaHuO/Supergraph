import copy
import sys
import time

"""
Problem B. Revenge of the Pancakes
"""

T = int( raw_input() )
ss = []
for i in xrange( T ):
    ss.append( raw_input() )

#----------------------------
def compare( r1, r2 ):
    return r1 if r2 == -1 or (  r1 > -1 and r1 < r2  ) else r2

rev_table = {
    '+': '-',
    '-': '+',
}

def solv( S ):

    xs = list( S )
    tokens = []
    last = xs[0]

    for s in xs[1:]:
        if last != s:
            tokens.append( last )

        last = s

    tokens.append( last )

    # print tokens

    size = len( tokens )
    return size if tokens[-1] == '-' else size -1


#----------------------------

start = time.clock()

res = []
for S in ss:
    res.append( solv( S ) )


i = 0
for r in res:
    i = i + 1
    print( "Case #{0}: {1}".format( i, r ) )

#end = time.clock()
#print end - start
sys.exit(0)
