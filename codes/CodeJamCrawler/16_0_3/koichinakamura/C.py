from math import sqrt
def solve(N, J):
    ans = []
    for n in xrange(2**(N-1)+1, 2**N-1, 2):
        s = bin(n)[2:]
        ds = []
        for b in range(2, 11):
            v = int(s, b)
            ok = False
            for k in [2,3,5,7]:
                if v % k == 0:
                    ds.append(k)
                    ok = True
                    break
            if not ok:
                break
        if len(ds) == 9:
            ans.append((n, ds))
        if len(ans) == J:
            break
    return ans

for case in range(input()):
    ans = solve(*map(int, raw_input().split()))

    print 'Case #{}:'.format(case+1)
    for b, ds in ans:
        print bin(b)[2:], ' '.join(map(str, ds))
