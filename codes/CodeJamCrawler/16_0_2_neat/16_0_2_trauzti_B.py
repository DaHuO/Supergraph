import random
import sys
import time
T = int(sys.stdin.readline())

swap = {"+":"-", "-":"+"}

#Reverse all pancakes
def reverse(pans):
    return "".join([swap[x] for x in pans[::-1]])

# Flip the first i pancakes.
def flip(pans, i):
    res = reverse(pans[:i]) + pans[i:]
    #print "flip(%s, %d)=%s" % (pans, i, res)
    return res


def solve(pans):
    count = 0
    plus = "+" * len(pans)
    minus = "-" * len(pans)
    if len(pans) == 1:
        if pans[0] == "-":
            return 1
        return 0
    while pans != plus and pans != minus:
        cliff = -1
        for i in xrange(len(pans)-1):
            if pans[i] != pans[i+1]:
                cliff = i
                break
        if cliff >= 0:
            pans = flip(pans, cliff+1)
            count += 1

    if pans == minus:
        pans = flip(pans, len(pans))
        count += 1
    return count


for tc in xrange(1, 1+T):
    pans = sys.stdin.readline()
    pans = pans.strip()
    c1 = solve(pans)
    c2 = 1 + solve(reverse(pans))
    print "Case #%d: %d" % (tc, min(c1,c2))
