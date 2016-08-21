#!/usr/bin/env python

def is_done(lookup):
    for i in range(10):
        if lookup[i] != 1:
            return False
    return True

def update_lookup(lookup,line):
    for i in line:
        lookup[ int(i) ] = 1
    return lookup 

def solve(line):
    if int(line) == 0:
        return 'INSOMNIA'
    
    lookup = [0 for i in range(10)]
    lookup = update_lookup(lookup,line)

    # if one presented?
    result = int(line)
    unit = result
    while not is_done(lookup):
        result = result + unit
        line = str(result)

        lookup = update_lookup(lookup,line)

    return result
        

if __name__ == '__main__':
    in_file = '../Downloads/A-large.in'
    in_file = open(in_file,'r')
    T = int(in_file.readline())
    
    out_file = open('out','w')
    i = 1
    for line in in_file:
        line = line[:-1]
        out_file.write('Case #%s: %s\n' % (i,solve(line)))   
        i = i + 1

    in_file.close()
    out_file.close()

