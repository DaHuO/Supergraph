#!/usr/bin/env python

import sys

# Cases
f = open(sys.argv[1])
cases = f.readlines()
len_cases = int(cases[0])

        
# Processing each case
for i in range(1, len_cases+1):

    # Initial number and factor
    S = cases[i].split('\n')[0]
    result = []
    for letter in S:
        if len(result) == 0:
            result += letter
        elif ord(letter) >= ord(result[0]):
            result = [letter] + result
        else:
            result.append(letter)
    print "Case #%d: %s" % (i, ''.join(result))
