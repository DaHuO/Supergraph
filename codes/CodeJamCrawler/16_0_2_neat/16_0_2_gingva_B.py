def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())


def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                pancakes = parseScalar(f,str)
                print pancakes
                x = solve(pancakes)
                print>>g, 'Case #%d: %s'  % (n+1,str(x))
                print 'Case #%d: %s'  % (n+1,str(x)  )


def switch(pan):
    pan = pan.replace('+','=')
    pan = pan.replace('-','+')
    pan = pan.replace('=','-')
    return pan
def flip(pan, c):
    return switch(pan[c-1::-1]) + pan[c:]
def active_stack(pan):
    return pan.rstrip('+')

def count_plus_prefix(pan):
    for i,v in enumerate(pan):
        if v == '-':
            return i
    return len(pan)

import sys, itertools
def solve(pancakes):
    flips = 0
    while True:
        pancakes = active_stack(pancakes)
        #print pancakes
        if not pancakes:
            return flips
        if pancakes[0] == '+': #flip the + prefix
            c = count_plus_prefix(pancakes)
            pancakes = flip(pancakes, c)
            #print 'flip plus', c, pancakes
            flips += 1
        # flip the whole stack
        pancakes = flip(pancakes, len(pancakes))
        #print 'flip whole', pancakes
        flips += 1

if __name__ == '__main__':
    #main('B-test.in', 'B-test.out')
    #main('B-small-attempt0.in', 'B-small-attempt0.out')
    main('B-large.in', 'B-large.out')
    sys.exit(0)


