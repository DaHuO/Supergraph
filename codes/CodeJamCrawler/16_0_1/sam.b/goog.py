def last(N):
    if not N: return 'INSOMNIA'
    Q = N
    all = set()
    while 1:
        for s in str(Q):
            all.add(s)
        if len(all) == 10: return Q
        Q += N

def inp(file1, file2):
    solns = []
    with open(file1) as f:
        T = int(f.readline().strip())
        for _ in range(T):
            solns.append(last(int(f.readline().strip())))

    with open(file2, 'w') as of:
        for i in range(T):
            of.write('case #%d: %s\n' % (i + 1, solns[i]))

inp('/Users/Shmu/Desktop/inal.txt', 'outfl.txt')