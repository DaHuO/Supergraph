#!/usr/bin/python
import sys


def execute():
    N=int(raw_input())
    for i in xrange(1,N+1):
        sys.stdout.write(''.join(["Case #",str(i),": "]))
        input = raw_input()
        cnt = 0
        upBelow = input[-1]=='+'
        i = 0
        while i < (len(input)-1):
            # print input[i], input[i+1]
            cnt += (input[i] != input[i+1])
            # print cnt
            i += 1
        cnt += not upBelow
        print cnt


execute()