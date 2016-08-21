#!/usr/bin/env python

import sys
import operator

def find_max(n_ppl, name_party):
    index, value = max(enumerate(n_ppl), key=operator.itemgetter(1))
    #print "\tfind_max %s %d" % (name_party[index], value)

    n_ppl[index] -= 1
    return name_party[index]

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
    n_party = int(raw_input())
    n_ppl = range(n_party)
    name_party = raw_input().split()
    #print "input str %s "% name_party
    cnt = 0
    result = ''
    for i in range(n_party):
        n_ppl[i] = int(name_party[i])
        cnt += n_ppl[i]
        name_party[i] = chr(ord('A')+i)

    #print "\tn ppl %s" % n_ppl
    #print "\tname_party %s "% name_party

    while (cnt > 0 ):
        if cnt == 3 or cnt == 1:
            result += find_max(n_ppl, name_party) +' '
            cnt -= 1
        else:
            result += find_max(n_ppl, name_party)
            cnt -= 1
            result += find_max(n_ppl, name_party) +' '
            cnt -= 1

    print "Case #%d: %s" %(case, result)

