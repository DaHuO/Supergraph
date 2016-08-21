def solve(N):
    if N == 0:
        return 'INSOMNIA'

    digits = [False]*10
    n = 1
    while True:
        for d in map(int, str(n*N)):
            digits[d] = True
        if all(digits):
            return n*N
        n += 1

for case in range(input()):
    ans = solve(input())
    print 'Case #{}: {}'.format(case+1, ans)
