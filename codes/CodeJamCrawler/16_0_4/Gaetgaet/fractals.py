T = int(input())


def alg(K, C, S):
    if S < K // C:
        return 'IMPOSSIBLE'
    else:
        sols = []
        power = C - 1
        sol = 0
        for s in range(K):
            sol += (s % K) * pow(K, power)
            power -= 1

            if power < 0:
                sols.append(sol + 1)
                sol = 0
                power = C - 1

        if power != C - 1:
            sols.append(sol + 1)
        return str(' '.join(map(str, sols)))

for t in range(T):
    K, C, S = map(int, input().split(' '))
    print('Case #{}: {}'.format(t + 1, alg(K, C, S)))
