def solve(l):
    new = []
    for sub in sorted(l):
        for s in sub:
            new.append(s)

    d = {}
    for n in new:
        d[n] = d.get(n,0)+1

    res = []
    for k,v in d.items():
        if v%2 != 0:
            res.append(k)
    res.sort()
    return " ".join(map(str, res))

def b():
    T = int(raw_input())
    for t in range(1,T+1):
        N = int(raw_input())
        p = []
        for n in range(2*N-1):
            positions = map(int,raw_input().split())
            p.append(positions)
        print "Case #{}:".format(t), solve(p)

if __name__ == '__main__':
    b()
