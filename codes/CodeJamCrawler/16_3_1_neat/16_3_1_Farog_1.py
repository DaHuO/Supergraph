#!/usr/bin/python
import os
import sys

from collections import Counter

T = int(raw_input())

import operator

def printSen(N, sens):
    parties = [chr(x) for x in range(65,65+N)]
    senators = {p:0 for p in parties}

    for p in range(0,len(parties)):
        senators[parties[p]] = sens[p]

    result = []

    SUM = float(sum(senators.values()))

    while SUM > 0:
        senators_sorted = sorted(senators.items(), key=operator.itemgetter(1), reverse=True)
        if SUM == 1:
            result.append(senators_sorted[0][0])
            senators[senators_sorted[0][0]] -= 1
        else:
            try:
                if (senators_sorted[1][1] / (SUM-2)) <= 0.5:
                    if (senators_sorted[0][1] >= 2):
                        result.append(senators_sorted[0][0]*2)
                        senators[senators_sorted[0][0]] -= 2
                    elif (senators_sorted[0][1] == 1):
                        if (N > 2) and senators_sorted[2][1] == SUM-2:
                            senators[senators_sorted[0][0]] -= 1
                            result.append(senators_sorted[0][0])
                        else:
                            senators[senators_sorted[0][0]] -= 1
                            senators[senators_sorted[1][0]] -= 1
                            result.append(senators_sorted[0][0] + senators_sorted[1][0])
                elif ((senators_sorted[0][1] / (SUM-2)) <= 0.5):
                    result.append(senators_sorted[1][0] * 2)
                    senators[senators_sorted[1][0]] -= 2
                elif (senators_sorted[0][1]-1) / (SUM - 2) <= 0.5:
                    if ((senators_sorted[1][1]-1) / (SUM - 2)) <= 0.5:
                        if (N > 2) and senators_sorted[2][1] == SUM - 2:
                            senators[senators_sorted[0][0]] -= 1
                            result.append(senators_sorted[0][0])
                        else:
                            result.append(senators_sorted[1][0] + senators_sorted[0][0] )
                            senators[senators_sorted[0][0]] -= 1
                            senators[senators_sorted[1][0]] -= 1

                elif (senators_sorted[1][1] / (SUM - 1)) <= 0.5:
                    if (senators_sorted[0][0] >= 1):
                        result.append(senators_sorted[0][0])
                        senators[senators_sorted[0][0]] -= 1
                elif (senators_sorted[0][1] / (SUM - 1)) <= 0.5:
                    senators[senators_sorted[1][0]] -= 1
                    result.append(senators_sorted[1][0])
            except Exception as e:
                if (SUM == 2):
                    if senators_sorted[0][1] == 2:
                        result.append(senators_sorted[0][0]*2)
                        senators[senators_sorted[0][0]] -= 2
                    elif senators_sorted[0][1] == 1:
                        result.append(senators_sorted[1][0] + senators_sorted[0][0])
                        senators[senators_sorted[0][0]] -= 1
                        senators[senators_sorted[1][0]] -= 1

        SUM = float(sum(senators.values()))

    return result

for i in range(1,T+1):
    sys.stdout.write(''.join(['Case #',str(i),': ']))
    N = int(raw_input())
    sens = [int(x) for x in raw_input().split()]
    res = printSen(N, sens)
    print ' '.join(res)


# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#   n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#   print "Case #{}: {} {}".format(i, n + m, n * m)
#   check out .format's specification for more formatting options