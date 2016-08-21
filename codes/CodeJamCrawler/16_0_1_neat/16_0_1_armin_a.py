from sys import stdin as inp

def next_int():
    return int(inp.readline().rstrip())

def digits(M):
    D = [0 for i in range(10)]
    if M == 0:
        D[0] = 1
        return D
    while M is not 0:
        D[M % 10] = 1
        M //= 10
    return D


T = next_int()
for cas in range(1,T+1):
    N = next_int()
    seen = [0 for i in range(10)]
    K = 1
    C = 0

    if N is 0:
        print("Case #{0:d}: INSOMNIA".format(cas))
    else:
        while True:
            C = K * N
            D = digits(C)
            seen = [max(seen[i], D[i]) for i in range(10)]
            if all(seen) == 1:
                break
            else:
                K += 1
        print("Case #{0:d}: {1:d}".format(cas, C))
