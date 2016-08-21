def solve(grid, maxi):
    d = {k: 0 for k in xrange( maxi + 1)}
    ans = []
    for j in grid:
        d[int(j)] += 1
    for k in d:
        if d[k] % 2 != 0:
            ans.append(k)
        else:
            continue
    ans.sort()
    ans = [str(ch) for ch in ans]
    return ' '.join(ans)


test_cases = int(raw_input())
for t in xrange(test_cases):
    mat = []
    a = []
    N = int(raw_input())
    # mat = str(raw_input())
    for i in xrange(2 * N - 1):
        # [mat.append(ch) for ch in str(raw_input()) if ch != ' ']
        mat.append(str(raw_input()))
    for j in mat:
        a.extend(j.split())
    mat = [int(ch) for ch in a]
    print "Case #%d: %s" % (t + 1, str(solve(mat, max(mat))))
