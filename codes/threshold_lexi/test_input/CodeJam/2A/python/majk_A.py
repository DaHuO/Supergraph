def comb(a,b):
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2],min(a[3],b[3])+max(a[3],b[3]))

MN=13
O=[{} for _ in range(MN+1)]
O[0] = {'R': (1,0,0,'R'), 'P': (0,1,0,'P'), 'S': (0,0,1,'S')}
for s in range(MN):
    O[s+1] = {
            'R': comb(O[s]['R'],O[s]['S']),
            'P': comb(O[s]['P'],O[s]['R']),
            'S': comb(O[s]['P'],O[s]['S'])
            }

T=int(input())
for t in range(T):
    N,R,P,S=map(int,input().split())
    ans = "IMPOSSIBLE"
    for v in O[N].values():
        if v[0] ==R and v[1]==P and v[2]==S:
            ans = v[3]
    print("Case #%d: %s" % (t+1,ans))
