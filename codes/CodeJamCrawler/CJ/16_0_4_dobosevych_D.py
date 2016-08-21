T = int(input())

for i in range(T):
    K, C, S = (int(_) for _ in input().split())
    lst = []
    if K != 1:
        for j in range(K):
            lst.append(str(j * ((K ** C - 1) // (K - 1)) + 1))
        print('Case #' + str(i + 1) + ': ' + ' '.join(lst))
    else:
        print('Case #' + str(i + 1) + ': 1')
