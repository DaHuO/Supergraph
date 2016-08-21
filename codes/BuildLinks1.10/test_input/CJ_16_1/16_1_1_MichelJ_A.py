"""
Code Jam 2016 Round 1A
Problem A. The Last Word
"""

from __future__ import print_function
import sys
import StringIO
from functools import partial
from autolog import logfunction

msg = partial(print, file=sys.stderr)

#===========================================================================

        
    

def doit(S):
    res = S[0]
    for l in S[1:]:
        if l >= res[0]:
            res = l + res
        else:
            res = res + l
    return res

sample = """7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE
"""

#===========================================================================

def stripnl(s):
    if s[-1]=="\n":
        return s[:-1]
    return s

def main(data = None):
    if data is None:
        f = sys.stdin
    else:
        f = StringIO.StringIO(data)
    nt = int(f.readline())
    for tc in xrange(1, nt+1):
        S = stripnl(f.readline())
        res = doit(S)
        msg( "Case #%d: %s" % (tc, res) )
        print( "Case #%d: %s" % (tc, res) )

main()
