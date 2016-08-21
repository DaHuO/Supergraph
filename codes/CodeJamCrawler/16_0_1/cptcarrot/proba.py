def add_seen(n, seen):
    for c in str(n):
        seen.add(c)
        
def get_last(N):
    k = 1
    if (N == 0):
        return 'INSOMNIA'
    seen = set()
    while len(seen) < 10:
        add_seen(k*N, seen)
        k += 1
    return str((k-1)*N)

def solve():
    infile = open("A-large.in")
    outfile = open("A-large.out", 'w')
    T = int(infile.readline().strip())
    for i in range(T):
        N = int(infile.readline().strip())
        res = "Case #%d: %s\n" % (i+1, get_last(N))
        outfile.write(res)
    infile.close()
    outfile.close()

solve()
