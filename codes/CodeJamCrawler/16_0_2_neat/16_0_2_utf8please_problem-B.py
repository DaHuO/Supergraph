#!/usr/bin/env python3

def solve(fin, fout):
    stack = list(fin.readline())[:-1]
    flip = 0
    last = '+'
    for bottom in range(len(stack) - 1, -1, -1):
        if stack[bottom] != last:
            flip += 1
        last = stack[bottom]
    
    fout.write(str(flip));
    fout.write('\n');
