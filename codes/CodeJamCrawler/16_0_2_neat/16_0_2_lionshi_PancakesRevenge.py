#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import groupby

def solve(S, b):
    if len(S) == 1:
        return 0 if S[0]==b else 1
    
    if S[-1]==b:
        return solve(S[:-1], b)
    else:
        return solve(S[:-1], S[-1]) + 1
        

def main():
    in_file = open("B-large.in", mode='r')
    out_file = open("B-large.out", mode='w')

    lines = in_file.readlines()      
    T = int(lines[0])
    
    for i in xrange(T):
        line = lines[i + 1].strip()
        S = [1 if s=='+' else 0 for s in line]
        S = [x[0] for x in groupby(S)]
        
        result = solve(S, 1) 
                
        out_file.write("Case #" + str(i+1) + ": " + str(result) + "\n") 
        
    in_file.close()
    out_file.close()


if __name__ == '__main__':
    main()
