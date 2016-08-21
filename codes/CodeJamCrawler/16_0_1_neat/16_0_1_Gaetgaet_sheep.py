T = int(input())


def alg(N):
    if N == 0:
        return 'INSOMNIA'
    else:
        digits = set([str(i) for i in range(10)])
        i = 1
        while len(digits) > 0:
            current = str(N * i)

            for char in current:
                try:
                    digits.remove(char)
                except KeyError:
                    pass
            i += 1
        return current

for t in range(T):
    N = int(input())
    print('Case #{}: {}'.format(t+1, alg(N)))