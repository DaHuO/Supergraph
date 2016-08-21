

import sys
stdin = sys.stdin

#from java.util import TreeMap


def solve(line, rev, fline, frev, first, length, flipped, order):
    #print first, length, order
    if 0 == length:
        return 0
    if length < 0:
        assert False
        return solve(rev, line, frev, fline, len(line)-first-1, -length,
                     flipped, order ^ 1)
    if flipped:
        return solve(fline, frev, line, rev, first, length, False, order ^ 2)

    if length == 1:
        if line[first] == '+':
            return 0
        return 1

        
    key = (first, length, order)
    if key in cache:
        return cache[key]

    #print "here", key
    #print first, length, line, line[first+length-1]
    if line[first+length-1] == '+':
        nlen = length-1
        while nlen > 0 and line[first+nlen-1] == '+':
            nlen -= 1
        rr = solve(line, rev, fline, frev, first, nlen, False, order)
        cache[key] = rr
        return rr

    best = 1e100
    for prefixlen in range(1, length):
        #print "prefixlen", prefixlen, length
        here = (1 + solve(line, rev, fline, frev, first, prefixlen, True, order)
                  + solve(rev, line, frev, fline, 
                          (len(line)-1-(first+length-1)),
                          (length - prefixlen), True, order ^ 1))
        best = min(best, here)


    cache[key] = best

    return best

def flip(plus_minuses):
    return ''.join('+' if c == '-' else '-' for c in plus_minuses)


T = int(stdin.readline().strip())
for icase in range(T):
    cache = {}

    line = stdin.readline().strip()
    rev = ''.join(reversed(line))
    fline = flip(line)
    frev = flip(rev)

    print 'Case #%d:' % (icase+1), solve(line, rev, fline, frev, 0, len(line),
                                         False, 0)
