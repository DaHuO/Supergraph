#!/usr/bin/env python

import os
import re
import sys
import json
import time
import shlex
import traceback
import subprocess

def findptm(st):
    last = '+'
    for i,s in enumerate(st):
        if st[i] == '-' and last == '+':
            return i
    return None

def flip(st, bottom):
    for i in range(bottom+1):
        st[i] = '-' if st[i] == '+' else '+'


def main():
    with open('B-small-attempt0.in.txt', 'r') as f: inp = f.read().split('\n')

    inp = inp[1:]
    for c,i in enumerate(inp):
        if not i: continue

        st = [ch for ch in i.strip()]
        lowest = len(st)-1
        count = 0
        while lowest>=0:
            if st[lowest] == '-':
                if st[0] == '+':
                    flipIndex = findptm(st)
                    flip(st, lowest)
                    count+=1
                else:
                    flip(st, lowest)
                    count+=1
            lowest -= 1

        print 'Case #'+str(c+1)+': '+str(count)

if __name__ == "__main__":
    main()