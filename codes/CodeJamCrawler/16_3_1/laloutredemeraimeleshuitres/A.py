def solve(L):
    D = { c: i for (i,c) in zip(L, 'ABCDEFGHIKLMNOPQRSTUVWXYZ') }
    s = []
    while D:
        m = max(D.values())
        e = [c for (c,i) in D.items() if i == m]
        if len(e) % 2:
            c = e[0]
            s.append(c)
            D[c] -= 1
            if D[c] == 0:
                del D[c]
        else:
            c,d = e[0],e[1]
            s.append(c+d)
            D[c] -= 1
            D[d] -= 1
            if D[c] == 0:
                del D[c]
            if D[d] == 0:
                del D[d]
    return ' '.join(s)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as f:
        T = int(f.readline())
        for i in range(T):
            N = int(f.readline())
            s = solve(map(int, f.readline().strip().split()))
            print 'Case #%d: %s'%(i+1, s)
