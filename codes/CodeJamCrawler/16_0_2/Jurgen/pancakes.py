# Author: Jurgen Nijland
# Date  : 9-4-2016

import sys

sys.stdin.readline()
counter = 0

for line in sys.stdin:
    counter += 1
    line = list(line.rstrip())
    S = len(line)

    pivot = S - 1
    cnt = 0
    while (pivot >= 0):
        if (line[pivot] == '-'):
            cnt += 1
            for i in range(0, pivot):
                if (line[i] == '-'):
                    line[i] = '+'
                else:
                    line[i] = '-'

        pivot -= 1
    print("Case #" + str(counter) + ": " + str(cnt))
