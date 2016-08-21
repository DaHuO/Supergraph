import fileinput
from itertools import permutations

def flip(stack,pos):
    flipped = ''.join(['-' if x=='+' else '+' \
        for x in list(stack[:pos+1])])
    return ''.join([flipped,stack[pos+1:]])

def ishappy(stack):
    for pancake in list(stack):
        if pancake == '-':
            return False;
    return True

def findflips(stack, ls, sz):
    if ishappy(stack):
        return 0
    cache = {}
    for i in range(1,sz+1):
        perm = permutations(ls, i)
        for p in perm:
            s = stack
            if p[:i-1] in cache:
                s = flip(cache[p[:i-1]],p[i-1])
            else:
                for pos in p:
                    s = flip(s,pos)
            cache[p] = s
            if ishappy(s):
                return i

t = int(raw_input())
for case in range(1,t+1):
    stack = raw_input()
    sz = len(stack)
    ls = [x for x in range(sz)]
    numflips = findflips(stack, ls, sz)
    print 'Case #{}: {}'.format(case, numflips)
