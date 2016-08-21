def getprob(p, f=0, a=0):
    n = len(p)
    m = f + a
    if n == m:
        # print("  "*m, "Till END")
        return 1
    if n - m == f - a:
        result = 1
        for i in range(m, n):
            result *= (1 - p[i])
        # print("  "*m, "END", m, result)
        return result

    if n - m == a - f:
        result = 1
        for i in range(m, n):
            result *= p[i]
        # print("  "*m, "END2", m, result)
        return result
    result = 0
    result += p[m] * getprob(p, f + 1, a)
    result += (1 - p[m]) * getprob(p, f, a + 1)
    # print("  "*m, result)
    return result

from itertools import combinations

t = int(input())
for case in range(1, t + 1):
    n, k = map(int, input().split())
    result = 0
    p = list(map(float, input().split()))
    for com in combinations(p, k):
        r = getprob(com)
        result = max(r, result)
    # k = int(k/2)
    # p.sort()
    # u = p[:k] + p[-k:]
    # print(u)
    # result = getprob(u)
    # for i in p[k:-k]:
    #     for j in range(2*k):
    #         u[j], i = i, u[j]
    #         r = getprob(u)
    #         u[j], i = i, u[j]
    #         if r > result:
    #             print("BAM!", i, u[j])

    print("Case #{}: {:.10f}".format(case, result))
