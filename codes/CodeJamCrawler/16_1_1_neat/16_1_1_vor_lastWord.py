#!/usr/bin/env python

def lastWord(s):
    curr = ''
    for letter in s:
        alt1 = letter + curr
        alt2 = curr + letter
        if alt1 > alt2:
            curr = alt1
        else:
            curr = alt2
    return curr

T = int(raw_input().strip())
for testCaseNo in range(T):
    s = raw_input().strip()
    print 'Case #' + str(testCaseNo + 1) + ':',
    print lastWord(s)
