lines = [line for line in open('insmall.in')]

for i in range(int(lines[0])):
    K, C, S = [int(v) for v in lines[i+1].split()]

    start = [j+1 for j in range(K)]

    if(C > K):
        C = K

    m = 0
    p = 1

    for c in range(C-1):
        result = []
        p = len(start)-2
        for x in start[:-1]:
            result.append(x*K - p)
            p = p-1

        start = result

    if(S<len(start)):
        print 'Case #%d: IMPOSSIBLE' % (i+1)
    else:
        print 'Case #%d: %s' % (i+1, " ".join(map(str, start)))
