#!/usr/local/bin/python3

from sys import stdin,stdout,stderr,exit

party = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

ncases = int(stdin.readline())

for case in range(1, ncases + 1):
    N = int(stdin.readline().strip())

    senate = []
    input = stdin.readline().strip().split(' ')
    for i in range(0, N):
        senate.append([party[i], int(input[i])])

    stdout.write('Case #%u: ' % (case))
    senate.sort(key=lambda x: x[1])

    while senate[-1][1] > 0:
        stdout.write('%s' % (senate[-1][0]))
        senate[-1][1] = senate[-1][1] - 1

        if (senate[-2][1] > 0) and not ((senate[-2][1] == 1) and (sum([x[1] for x in senate]) == 2)):
            stdout.write('%s' % (senate[-2][0]))
            senate[-2][1] = senate[-2][1] - 1

        stdout.write(' ')
        senate.sort(key=lambda x: x[1])

    stdout.write('\n')
