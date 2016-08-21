import numpy as np
import sys
import string

def solve(s):
    ans=''
    for ele in s:
        if len(ans)==0 or ele>=ans[0]:
            ans = ele+ans
        else:
            ans=ans+ele
    return ans

f = open(sys.argv[1])

f.readline()
for e,ln in enumerate(f):
    print "Case #"+str(e+1)+': '+solve(ln),
