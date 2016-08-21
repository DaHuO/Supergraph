import sys
import StringIO

def make_array(S):
    return [1 if a=="+" else 0 for a in S]

def first0(a):
    for i, v in enumerate(a):
        if v==0:
            return i
    return -1

def last0(a):
    for i in xrange(len(a)-1, -1, -1):
        if a[i]==0:
            return i
    return -1

def n_leading1(a):
    for i, v in enumerate(a):
        if v!=1:
            return i
    return len(a)

def flip(a, n):
    b = a[:]
    for i in xrange(n):
        b[i] = 1 - a[n-i-1]
    return b

def doit(S):
    a = make_array(S)
    n_flips = 0
    f0 = first0(a)
    while f0 >= 0:
#        print a
        if f0!=0:
            nl1 = n_leading1(a)
            a = flip(a, nl1)
        else:
            l0 = last0(a)
            a = flip(a, l0+1)
        n_flips += 1
        f0 = first0(a)
    return str(n_flips)

sample = """5
-
-+
+-
+++
--+-
"""

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
    for tc in xrange(nt):
        S = stripnl(f.readline())
        print "Case #%d: %s" % (tc+1, doit(S))

main()
