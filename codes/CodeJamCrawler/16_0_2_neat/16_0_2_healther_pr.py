import sys
#import argpase

import numpy as np 

transtable = str.maketrans('+-','-+')

def swap(inputline, n, i):
    outputline = inputline[:n].translate(transtable) + inputline[n:]
    return outputline, i+1



def number_of_swaps(inputline):
    line = inputline

    nswaps = 0
    while '-' in line:
        if line.startswith('+'):
            try:
                n = line.index('-')
            except ValueError:
                n = len(line)
            line, nswaps = swap(line, n, nswaps)
        else:
            try:
                n = line.index('+')
            except ValueError:
                n = len(line)
            line, nswaps = swap(line, n, nswaps)

    return "{}".format(nswaps)



if "__main__" == __name__:
    
    print(sys.argv[1])
    inputfile = sys.argv[1]

    out = []
    with open(inputfile, 'r') as f:
        T = int(f.readline())
        for _ in range(T):
            out.append(number_of_swaps(f.readline()))
    
    with open("out_"+inputfile, 'w') as f:
        for i, o in enumerate(out):
            f.write("Case #{}: {}\n".format(i+1, o))
            print("Case #{}: {}".format(i+1, o))
