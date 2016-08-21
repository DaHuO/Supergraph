def solve(K, C, S):
    if K // C > S:
        return 'IMPOSSIBLE'
    check = range(K)
    splits = []
    while check:
        cur = check[:C]
        check = check[C:]
        splits.append(sum(c*K**i for i, c in enumerate(cur)) + 1)
    return ' '.join(map(str, splits))

#  inp = list(open('d-sample.in'))[1:]
inp = list(open('D-small-attempt0.in'))[1:]
#  inp = list(open('D-large.in'))[1:]
for t, s in enumerate(inp):
    print 'Case #%d: %s' % (t+1, solve(*list(map(int, s.split()))))
