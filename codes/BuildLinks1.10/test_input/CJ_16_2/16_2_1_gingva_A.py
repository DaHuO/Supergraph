def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())


def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                N = parseScalar(f,str)
                print N
                x = solve(N)
                print>>g, 'Case #%d: %s'  % (n+1,str(x))
                print 'Case #%d: %s'  % (n+1,str(x)  )

def issubset(c1,c2):
    if not set(c1.keys()).issubset(set(c2.keys())):
        return False
    diff = c2-c1
    k = len(diff)
    diff += Counter()
    return k == len(diff)


def recSearch(hist, searchNei, partSol):
    letters = set(hist.keys())
    # test matching neighbours
    #print searchNei
    #print hist
    searchNei2 = [(w,c) for (w,c) in searchNei if issubset(c,hist)]
    #print searchNei2
    if len(searchNei2) == 0:
        return None

    for w,c in searchNei2:
        hist2 = hist + Counter()
        print 'adding', w,
        z=0
        while issubset(c,hist2):
            hist2 = hist2 - c
            hist2 += Counter()
           # print hist, c, hist2
            z+=1
        print '*', z
        print hist2
        if len(hist2) == 0:
            return partSol + [mapD[w]]*z
        sol = recSearch(hist2, searchNei2, partSol + [mapD[w]]*z)
        if sol is not None:
            return sol

    return None


digits = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
mapD = dict((w,i) for (i,w) in enumerate(digits))

import sys, itertools
from collections import Counter
def solve(seq):

    hist = Counter(seq)


    res = []
    # trivially identify all single digits
    triv = [('Z','ZERO'), ('W','TWO'), ('X','SIX'), ('G','EIGHT')]
    for letter,word in triv:
        for i in range(hist[letter]):
            res.append(mapD[word])
            for k in word:
                hist[k] -= 1
    hist += Counter()

    searchNei = set(digits) - set(w for (l,w) in triv)
    searchNei = [(w,Counter(w)) for w in searchNei]

    if len(hist) > 0:
        res2 = recSearch(hist, searchNei, [])
        res = res + res2
    res.sort()
    return ''.join(str(x) for x in res)

if __name__ == '__main__':
    #main('A-test.in', 'A-test.out')
    #main('A-small-attempt0.in', 'A-small-attempt0.out')
    main('A-large.in', 'A-large.out')
    sys.exit(0)


