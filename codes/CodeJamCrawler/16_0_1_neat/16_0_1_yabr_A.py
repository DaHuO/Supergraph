def func(N):
    if N == 0:
        return "INSOMNIA"

    seenDigits = [False] * 10
    factor = 1

    while seenDigits.count(False) > 0:
        digits = str(factor * N)

        for d in digits:
            seenDigits[int(d)] = True

        factor += 1

    return N * (factor - 1)

T = int(input())

for t in range(T):
    N = int(input())
    print('Case #' + str(t+1) + ': ' + str(func(N)))

