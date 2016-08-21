in_file = 'A-large.in'
out_file = 'A-small-attempt0.out'



def solve(fin, fout):
    T = int(fin.readline().strip())
    for _t in range(1, T + 1):
        N = int(fin.readline().strip())
        tmp = map(int, fin.readline().strip().split())
        P = []
        idx = 0
        for i in tmp:
            P.append([i, chr(ord('A') + idx)])
            idx += 1
        P.sort()
        res = []
        while P[N - 1][0] != 0:

            if (P[N - 1][0] == P[N - 2][0]):
                if (N >= 3 and P[N - 2][0] > P[N - 3][0]) or (N < 3):
                    P[N - 1][0] -= 1;
                    P[N - 2][0] -= 1;
                    res.append([P[N - 1][1], P[N - 2][1]])
                else:
                    P[N - 1][0] -= 1;
                    res.append([P[N - 1][1],])
            else:
                P[N - 1][0] -= 1;
                res.append([P[N - 1][1],])
            P.sort()
        tmp = []
        for item in res:
            tmp.append(''.join(item))
        fout.write('Case #%d: %s\n' % (_t, ' '.join(tmp)))





with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
    solve(fin, fout)