#!/usr/bin/env python

import os
import re
import sys
import json
import time
import shlex
import traceback
import subprocess

def main():
    with open('input.txt', 'r') as f:
        inp = f.read().split('\n')
    inp = inp[1:]
    for c,i in enumerate(inp):

        if not i: continue
        number = int(i)
        m = 1
        counted = []
        while True:
            newNumber = str(number*m)
            #print newNumber
            if m>1 and int(newNumber) == number:
                m = 'INSOMNIA'
                break
            counted += [int(n) for n in newNumber[:]]
            #print set(counted)
            if len(set(counted))==10:
                m *= number
                break
            m += 1

        print 'Case #'+str(c+1)+': '+str(m)

if __name__ == "__main__":
    main()