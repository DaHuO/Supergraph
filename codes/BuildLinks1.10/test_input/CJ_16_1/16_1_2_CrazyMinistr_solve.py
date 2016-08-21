fi = open('in', 'r')
fo = open('out', 'w')

T = int(fi.readline())
for t in range(T):
    n = int(fi.readline())
    cnt = [0] * 3000
    for i in range(2 * n - 1):
        for s in fi.readline().split():
            cnt[int(s)] += 1

    ans = []
    for i, j in enumerate(cnt):
        if j % 2:
            ans.append(i)

    # a = sorted(a)
    # print(a)
    # res = []
    # for i in range(n):
    #     res.append([0] * n)
    #
    # ind = 0
    # ans = ['HABEBE']
    # magic = 0
    # for i in range(0, len(a), 2):
    #     x = a[i]
    #     if i == 2 * n - 2:
    #         for j in range(ind):
    #             if x[j] != res[ind][j]:
    #                 for k in range(n):
    #                     res[k][ind] = x[k]
    #                 ans = res[n - 1]
    #         else:
    #             ans = []
    #             res[n - 1] = x
    #             for j in range(n):
    #                 ans.append(res[j][n - 1])
    #         break
    #
    #     y = a[i + 1]
    #     if magic == 0:
    #         res[ind] = x
    #         for j in range(n):
    #             res[j][ind] = y[j]
    #     else:
    #         res[ind] = y
    #         for j in range(n):
    #             res[j][ind] = x[j]
    #
    #     ind += 1
    #     magic = 1 - magic
    #
    fo.write('Case #{}: {}\n'.format(t + 1, ' '.join(str(s) for s in ans)))
    # for r in res:
    #     print(' '.join(str(s) for s in r))
    # print('')
    #
