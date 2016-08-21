def solve(pa):
    flips = 0
    curr = '+'
    for i in range(len(pa)-1, -1, -1):
        if pa[i] != curr:
            flips += 1
            curr = pa[i]
    return flips

inp = open('B-large.in')
outp = open('Blarge.out', 'w')

T = int(inp.readline())

for i in range(1, T+1):
    pa = inp.readline().rstrip()
    outp.write('Case #{}: {}\n'.format(i, solve(pa)))
    print solve(pa)

inp.close()
outp.close()
