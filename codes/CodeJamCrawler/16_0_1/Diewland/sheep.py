#!/usr/bin/python

##########################################################

def process(line):
    v = int(line)
    if v == 0:
        return 'INSOMNIA'
    else:
        round = 1
        target = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        while(True):
            vv = v * round
            for c in str(vv):
                c = int(c)
                if c in target:
                    target.remove(c)
            #print round, vv, target
            if(len(target) == 0):
                return vv
            round += 1

##########################################################

import sys
total_cases = None
case_no = 1
with open(sys.argv[1]) as f:
    for line in f:
        if total_cases is None:
            total_cases = int(line)
        else:
            """
            if case_no != 85:
                case_no += 1
                continue # TODO
            print line
            """
            result = process(line.strip())
            print "Case #%s: %s" % ( case_no, result )
            case_no += 1
