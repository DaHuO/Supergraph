#!/usr/bin/env python

def solve(line):
    ops = 0
    if line[0] == '+':
        # find first negetive
        first_negetive = -1
        for i in range(len(line)):
            if line[i] == '-':
                first_negetive = i
                break

        if first_negetive == -1:
            # all positive
            return 0
        
        # rebuild line
        line = ''.join(['-' for i in range(first_negetive)]) + line[first_negetive:]
        ops = ops + 1
    
    # find first positive
    first_positive = -1
    for i in range(len(line)):
        if line[i] == '+':
            first_positive = i
            break

    # no positive
    if first_positive == -1:
        return ops + 1
    
    # retbuild line
    line = line[first_positive:-1] + ''.join(['+' for i in range(first_positive)])
    ops = ops + 1
    return ops + solve(line)

if __name__ == '__main__':
    in_file = '../Downloads/B-large.in'
    in_file = open(in_file,'r')
    T = int(in_file.readline())
    
    out_file = open('out','w')
    i = 1
    for line in in_file:
        out_file.write('Case #%s: %s\n' % (i,solve(line)))   
        i = i + 1

    in_file.close()
    out_file.close()

