def sol(N):
    if N == 0:
        return 'INSOMNIA'

    i, K = 0, N
    s = set()
    while len(s) < 10:
        i, K = i + 1, N * (i + 1)
        s.update([x for x in str(K)])

    return K

T = int(raw_input())
for i in range(T):
    n = int(raw_input())
    print("Case #{0}: {1}".format(i+1, sol(n)))
