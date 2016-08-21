def rank(a):
    hist = {}
    for row in a:
        for e in row:
            hist[e] = hist.get(e,0)+1
    odd_els = []
    for k,v in hist.items():
        if v%2:
            odd_els.append(k)
    return " ".join(map(str,sorted(odd_els)))
    
t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    ranks = []
    for r in range(2*n-1):
        ranks.append(map(int, raw_input().split()))
    print "Case #{}: {}".format(i+1, rank(ranks))
