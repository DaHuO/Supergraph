
def solve(x):
    i = 0
    d = [0]*10    
    while any(p==0 for p in d) and i < 20000000:
        i += 1
        for p in map(int, str(x*i)):
            d[p] += 1
        
    assert(all(p>0 for p in d))
    print(i, d, x*i)
    return x*i

with open("output.txt", "w") as f:
    for i,l in enumerate(open("A-large.in").readlines()[1:]):        
        res = 'INSOMNIA'
        try:
            res = solve(int(l))
        except AssertionError:
            pass
        print('Case #{}: {}'.format(i+1, res), file=f)

        
