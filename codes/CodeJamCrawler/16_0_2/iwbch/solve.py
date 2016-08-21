#!/usr/bin/python

import sys
from pprint import pprint

def solve(cakes):
    #pprint(cakes)
    num = 0
    while '-' in cakes:
        f_p_pos = 0
        for i in xrange(len(cakes)):
            if cakes[i] == '-':
                break
        f_p_pos = i
        #print f_p_pos
        if i > 0:
            #print 'front maeuver'
            cakes = maneuver(cakes[0:f_p_pos]) + cakes[f_p_pos:]
            num += 1
            continue

        c_len = len(cakes)
        l_p_pos = c_len
        for i in xrange(c_len):
            pos = c_len - 1 - i
            if cakes[pos] == '-':
                l_p_pos = pos + 1
                break
        #print 'maeuver'
        #print l_p_pos
        cakes = maneuver(cakes[0:l_p_pos])
        num += 1

    return num

def maneuver(cakes):
    #pprint(cakes)
    tmp = ''
    for c in cakes[::-1]:
        tmp += '+' if c == '-' else '-'
    #pprint(tmp)
    return tmp

if __name__ == '__main__':

    case_N = int(sys.stdin.readline().strip())
    #pprint(case_N)
    for n in xrange(case_N):
        cakes = sys.stdin.readline().strip()
        ans = solve(cakes)
        print 'Case #' + str(n+1) + ': ' + str(ans)
