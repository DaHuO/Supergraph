T = input()

def solve(N):
    if N == 0:
        return 'INSOMNIA'
    dig = set()
    m = 0
    while len(dig) < 10:
        m += 1
        dig.update(c for c in str(m * N))
    return m * N

for i in range(1, T + 1):
    print 'Case #{}: {}'.format(i, solve(input()))
