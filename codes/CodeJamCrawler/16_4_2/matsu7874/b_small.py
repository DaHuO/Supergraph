import itertools
TESTCASE = int(input())

for test in range(TESTCASE):
    n,k = map(int, input().split())
    ps = list(map(float, input().split()))
    ps.sort()
    p = [[0 for j in range(k+1)] for i in range(k+1)]
    # cmt = []
    # for i in range(k//2):
    #     cmt.append(i)
    #     cmt.append(n-i-1)
    max_p = 0
    for cmt in itertools.combinations(list(range(n)),k):
        p = [[0 for j in range(k+1)] for i in range(k+1)]
        p[0][0] = 1
        for i in range(k):
            for j in range(k):
                p[i+1][j+1] += p[i][j] * ps[cmt[i]]
                p[i+1][j] += p[i][j] * (1-ps[cmt[i]])
        max_p = max(max_p, p[k][k//2])
    print('Case #' + str(test + 1) + ':',max_p)
