T = int(raw_input())

for qw in range(1, T+1):
    print 'Case #%d:' % qw,
    N, R, P, S = map(int, raw_input().split(' '))
    opt = ('R', 'P', 'S')
    options = []
    for start in opt:
        state = [[start]]
        for i in range(N):
            last = state[-1]
            cur = []
            state.append(cur)
            for x in last:
                if x == 'R':
                    if i == N - 1:
                        cur.append('R')
                        cur.append('S')
                    else:
                        cur.append('S')
                        cur.append('R')
                elif x == 'P':
                    cur.append('P')
                    cur.append('R')
                else:
                    cur.append('P')
                    cur.append('S')
        if len([r for r in cur if r == 'R']) == R and (
                len([p for p in cur if p == 'P']) == P and (
                    len([s for s in cur if s == 'S']) == S)):
            for sz in [2**x for x in range(N)]:
                for j in range(0, len(cur), sz*2):
                    a = cur[j:j+sz]
                    b = cur[j+sz:j+2*sz]
                    if ''.join(b) < ''.join(a):
                        for k in range(sz):
                            tmp = cur[j+k]
                            cur[j+k] = cur[j+k+sz]
                            cur[j+k+sz] = tmp
                    else:
                        pass
                        #print ''.join(a), ''.join(b)
            print ''.join(cur)
            break
    else:
        print 'IMPOSSIBLE'
