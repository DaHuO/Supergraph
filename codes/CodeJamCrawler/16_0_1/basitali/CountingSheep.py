def count(N):
    digits = set([str(i) for i in range(10)])
    index = 1
    multiple = N
    while len(digits) > 0:
        multiple = index * N
        if index > 1 and multiple == N:
            return "INSOMNIA"
        digits = digits - set([i for i in str(multiple)])
        index += 1

    return str(multiple)

if __name__ == '__main__':
    case = 'A-large'
    inp = open('%s.in'%case);
    out = open('%s.out'%case, 'w');

    cases = int(inp.readline())
    for i in xrange(1, cases + 1):
        n = int(inp.readline())
        o = "Case #%d: %s"%(i, count(n))
        print o
        out.write('%s'%o)
        if i < cases:
            out.write('\n')
