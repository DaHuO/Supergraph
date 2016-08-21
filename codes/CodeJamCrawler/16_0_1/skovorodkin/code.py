def solve(N):
    if N == 0:
        return
    fin = {str(x) for x in range(10)}
    cur = set()
    n = N
    i = 1
    while True:
        cur.update(str(n))
        if cur == fin:
            return N * i

        i += 1
        n = N * i

T = int(input())
for _ in range(T):
    n = int(input())
    print('Case #{}: '.format(_+1), solve(n) or 'INSOMNIA')
