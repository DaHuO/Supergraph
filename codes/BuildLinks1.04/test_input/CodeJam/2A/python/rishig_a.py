import sys

def swap(s, a, b, w):
    if s[a:a+w] > s[b:b+w]:
        return s[:a] + s[b:b+w] + s[a+w:b] + s[a:a+w] + s[b+w:]
    else: return s

def bsort(s,N):
    for i in range(1, N+1):
        for a in range(0, 2**N, 2**i):
            s = swap(s, a, a+2**(i-1), 2**(i-1))
    return s

def expand(s):
    def f(x):
        if x == 'P': return 'PR'
        if x == 'R': return 'RS'
        if x == 'S': return 'SP'
    return ''.join(f(x) for x in s)

class RPS:
    def __init__(self, trip, s, N):
        self.trip = trip
        self.s = s
        self.N = N

    def nxt(self):
        ns = bsort(expand(self.s), self.N+1)
        x,y,z = self.trip
        ntrip = (x+y, y+z, x+z)
        return RPS(ntrip, ns, self.N+1)

# def RPSnxt(R,P,S):
#     x = (R + S - P) / 2
#     y = (R + P - S) / 2
#     z = (P + S - R) / 2
#     if x < 0 or y < 0 or z < 0:
#         return None
#     return (x,y,z)


def getd():
    d = {}
    cur = [RPS((1,0,0), 'R', 0), RPS((0,1,0), 'P', 0), RPS((0,0,1), 'S', 0)]
    for i in range(13):
        for k in range(3):
            d[cur[k].trip] = cur[k].s
            cur[k] = cur[k].nxt()
    return d

fin = file(sys.argv[1])
T = int(fin.readline().strip())
d = getd()
for i in range(1,T+1):
    N,R,P,S = [int(x) for x in fin.readline().strip().split()]
    ans = d.get((R,P,S), 'IMPOSSIBLE')
    print('Case #%d: %s' % (i, ans))
