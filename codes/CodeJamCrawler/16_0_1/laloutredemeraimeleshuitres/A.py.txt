def solve(N):
    if not N: return 'INSOMNIA'
    seen = set()
    i = 1
    while True:
        seen |= set(str(i*N))
        if len(seen) == 10:
            return i*N
        else:
            i+= 1

def A(filename):
    f = open(filename)
    r = open(filename+'.res', 'w')
    T = int(f.readline())
    for i in range(1, T+1):
        N = int(f.readline())
        r.write('Case #{}: {}\n'.format(i, solve(N)))