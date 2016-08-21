#!/usr/bin/env python

import sys

# Cases
f = open(sys.argv[1])
cases = f.readlines()
len_cases = int(cases[0])

# Verify if every entry in dict as >1 value
def verifyDico(dico):
    if 0 in dico.values():
        return True
    else:
        return False
        
# Processing each case
for i in range(1, len_cases+1):

    # Initial number and factor
    N = int(cases[i])
    factor = 0
    tested = N

    # Initial dict
    dico = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    if N == 0:
        print "Case #%d: INSOMNIA" % (i)
    else:
        while verifyDico(dico):
            factor += 1
            tested = factor*N
            for ch in str(tested):
                dico[int(ch)] += 1
        print "Case #%d: %d" % (i, tested)
