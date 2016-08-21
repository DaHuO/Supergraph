
def getPattern(p, C):
    P = p
    for i in range(1, C):
        # print(i, P)
        Pnext = ''
        for c in P:
            if c == 'G':
                Pnext += 'G' * len(p)
            else:
                Pnext += p
        P = Pnext
        # print(i, P)
    return P

def printEnumeration(K, C):
    for i in range(2 ** K):
        basePattern = ("{0:0" + str(K) + "b}").format(i)
        basePattern = basePattern.replace('1', 'G')
        basePattern = basePattern.replace('0', 'L')
        print(basePattern, getPattern(basePattern, C))

def getMinSteps(K, C):
    c = C
    if c > K:
        c = K
    return (K + 1) - c

def isPossible(min, S):
    return S >= min

def decodeLocation(K, C, comb):
    # print(comb)
    s = 0
    for i, Ai in enumerate(comb, start=1):
        # print('(%d - 1) * (%d ** (%d - %d))' % (Ai, K, C, i))
        s += (Ai - 1) * (K ** (C - i))
    s += 1
    return s

def chooseLocations(K, C):
    loc = []
    minSteps = getMinSteps(K, C)
    c = C
    if c > K:
        c = K
    for i in range(1, minSteps + 1):
        choices = range(i, c + i)
        loc.append(decodeLocation(K, C, choices))
    return loc

def main():
    numInputs = int(input())
    for i in range(numInputs):
        K, C, S = (int(c) for c in input().split(' '))
        if not isPossible(getMinSteps(K, C), S):
            print("Case #%d: IMPOSSIBLE" % (i + 1))
        else:
            steps = ' '.join([str(l) for l in chooseLocations(K, C)])
            print("Case #%d: %s" % (i + 1, steps))

if __name__ == '__main__':
    import sys
    if '-d' in sys.argv:
        pass
    else:
        main()