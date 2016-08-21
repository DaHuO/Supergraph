#!/usr/bin/env python

import sys

def pancake(pan):
    cur = pan[0]
    l = [[cur]]
    k = 0
    i = 1
    while(i < len(pan)):
        if(pan[i] == cur):
            l[k].append(pan[i])
        else:
            cur = pan[i]
            k += 1
            l.append([pan[i]])
        i += 1
    return l

def process(groups):
    if(groups[-1][0] == '+'):
        groups = groups[:-1]
    if(len(groups) == 0):
        return 0
    return len(groups)

if __name__ == "__main__":
    for (k, i) in enumerate([l.rstrip("\n") for l in sys.stdin.readlines()[1:]]):
        s = str(process(pancake(i)))
        print("Case #" + str(k + 1) + ": " + s)
