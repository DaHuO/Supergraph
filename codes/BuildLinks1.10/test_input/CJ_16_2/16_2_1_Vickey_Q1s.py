#!/usr/bin/env python

import os
import re
import sys
import json
import copy
import time
import math
import shlex
import traceback
import subprocess


def debug(string):
    if True: print str(string)

outStr = ''
def output(string):
    print string
    global outStr
    outStr += string+'\n'


nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def rem(maps, numind):
    out = []
    for n in range(numind, len(nums)):
        print range(numind, len(nums))
        mapsc = copy.copy(maps)
        allTrue = True
        for p in nums[n]:
            if not mapsc.get(p):
                allTrue = False
                break
            if mapsc[p]-1<0:
                allTrue = False
                break
            mapsc[p] -= 1

        if allTrue:
            debug(numind)
            debug(mapsc)
            allTrue = True
            for m in mapsc:
                if mapsc[m] != 0:
                    allTrue = False

            if allTrue: return [n]

            out += [n]

            ret = rem(mapsc, n)
            if ret == []: out = []
            else:   return out+ret

    return out


def main():
    #with open('input.txt', 'r') as f: inp = f.read().split('\n')
    with open('A-small-attempt2.in.txt', 'r') as f: inp = f.read().split('\n')
    #with open('A-large-practice.in.txt', 'r') as f: inp = f.read().split('\n')

    inp = inp[1:]
    for c,i in enumerate(inp):
        if not i: continue

        parts   = [n for n in i.split()]
        debug(parts)

        

        maps = {}

        for p in parts[0]:
            if maps.get(p):
                maps[p] += 1
            else:
                maps[p] = 1
        debug(maps)
        out = [str(i) for i in rem(maps, 0)]

        output('Case #'+str(c+1)+': '+str(''.join(out)))

    with open('output.txt', 'w') as f: f.write(outStr)

if __name__ == "__main__":
    main()