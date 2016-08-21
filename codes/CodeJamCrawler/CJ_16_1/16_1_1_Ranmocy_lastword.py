def solve(s):
    result = []
    for c in s:
        if len(result) == 0:
            result.append(c)
        elif c < result[0]:
            result.append(c)
        else:
            result.insert(0, c)
    return ''.join(result)

with open('lastword.in', 'r') as fin:
    with open('lastword.out', 'w') as fout:
        T = int(fin.readline())
        for i in xrange(1, T+1):
            fout.write('Case #{0}: {1}'.format(i, solve(fin.readline())))
