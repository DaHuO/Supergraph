def solve():
    infile = open('D-small-attempt0.in')
    outfile = open('D-small-attempt0.out', 'w')
    T = int(infile.readline().strip())
    for i in range(T):
        K, C, S = map(int, infile.readline().strip().split())
        res = ' '.join(map(str, range(1, K+1)))
        outfile.write("Case #%d: %s\n" % (i+1, res))
    infile.close()
    outfile.close()
    
solve()
