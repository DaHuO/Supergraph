import sys
#import argpase

import numpy as np 


def friendsneeded(shynessfrequency):
    npshy = np.array( [int(c) for c in shynessfrequency] )
    npshycum = npshy.cumsum()
    pplstanding = npshycum[0]
    additional = 0
    for i in range(len(npshy))[1:]:
        pplstanding = npshycum[i-1]+additional
        if i>pplstanding:
            additional += i - pplstanding
    return additional

def getdigits(number):
    size = int(np.log10(number)) + 1
    digits = []
    for s in range(size):
        digit = number // 10**s % 10
        digits.append(digit)
    return digits

def count(inputline):
    orgnumber = int(inputline)
    if orgnumber==0:
        return "INSOMNIA"
    
    # find max digit
    seendigits = set()
    n = 0
    while len(seendigits)<10:
        n += 1
        number = n*orgnumber
        digits = getdigits(number)
        for d in digits:
            seendigits.add(d)

    return "{}".format(number)



if "__main__" == __name__:
    
    print(sys.argv[1])
    inputfile = sys.argv[1]

    out = []
    with open(inputfile, 'r') as f:
        T = int(f.readline())
        for _ in range(T):
            out.append(count(f.readline()))
    
    with open("out_"+inputfile, 'w') as f:
        for i, o in enumerate(out):
            f.write("Case #{}: {}\n".format(i+1, o))
            print("Case #{}: {}\n".format(i+1, o))
    print(out)