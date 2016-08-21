from itertools import permutations

t = int(raw_input())
for testCase in range(1, t + 1):
    n = int(raw_input())
    f = list(map(lambda x: int(x) - 1, raw_input().split()))
    ans = 0
    for p in permutations(range(n)):
        for ln in range(1, n + 1):
            cur = list(p[:ln])
            if ln > 2 and not(f[cur[ln - 2]] in (cur[ln - 1], cur[ln - 3])):
                break
            if ln <= ans:
                continue
            if ln == 1:
                flag = f[cur[0]] == cur[0]
            else:
                flag = (f[cur[0]] in (cur[1], cur[ln - 1])) and \
                       (f[cur[ln - 1]] in(cur[ln - 2], cur[0]))
            if flag and ln > ans:
                ans = ln
    print 'Case #' + str(testCase) + ': ' + str(ans)
