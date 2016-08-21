T = int(raw_input())

for case in range(T):
    K, C, S = map(int, raw_input().split(' '))

    current = 1
    answer = []
    step = K**(C - 1)
    for i in range(K):
        answer.append(current)
        current += step

    print "Case #{}: {}".format(case + 1, ' '.join(map(str, answer)))
