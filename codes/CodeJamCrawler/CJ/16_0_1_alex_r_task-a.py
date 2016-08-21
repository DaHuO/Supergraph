def solve(N):
    if N == 0:
        return None
    digits = [False] * 10
    k = N
    while True:
        l = 1
        r = 10
        while k // l > 0:
            d = (k % r) // l
            digits[d] = True
            l *= 10
            r *= 10
        all = True
        for i in range(10):
            if not digits[i]:
                all = False
        if all:
            return k
        k += N

answers = []

with open('A-small-attempt0.in') as inputFile:
    T = int(inputFile.readline())
    for i in range(T):
        N = int(inputFile.readline())
        s = solve(N)
        if not s:
            answers.append('INSOMNIA')
        else:
            answers.append(s)

with open('A-small-attempt0.out', 'w') as outputFile:
    for ind, ans in enumerate(answers):
        line = 'Case #{0}: {1}\n'.format(ind+1, ans)
        outputFile.write(line)
