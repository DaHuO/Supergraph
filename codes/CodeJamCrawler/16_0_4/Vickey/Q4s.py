#!/usr/bin/env python

import os
import re
import sys
import json
import time
import math
import shlex
import traceback
import subprocess

def main():
    #with open('input.txt', 'r') as f: inp = f.read().split('\n')
    with open('D-small-attempt0.in.txt', 'r') as f: inp = f.read().split('\n')

    inp = inp[1:]
    for c,i in enumerate(inp):
        if not i: continue

        K = i.strip().split(' ')
        C = int(K[1])
        S = int(K[2])
        K = int(K[0])

        if C == 1:  reqd = K
        else:       reqd = K - pow(2,C-2)
        if reqd <= 0: reqd = 1

        ans = []

        ans = range(1,K+1)
        ans = [str(a) for a in ans]
        '''
        for r in range(reqd/2):
            ans += [r+2]
            ans += [pow(K,C)-r-1]
        if reqd&1:
            ans += [pow(K,C)/2+1]
        '''
        if len(ans)>S:
            ans = ['IMPOSSIBLE']

        print 'Case #'+str(c+1)+': '+' '.join(ans)

if __name__ == "__main__":
    main()