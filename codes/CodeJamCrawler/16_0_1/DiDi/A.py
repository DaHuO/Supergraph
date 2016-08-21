T = int(input())


def f(N):
    if N == 0:
        return ("INSOMNIA")
    if N > 0:
        finished = False
        total = set()
        K = 1
        while True:
            m = K*N
            c = set(str(m))
            total = total.union(c)
            if len(total)== 10:
                finished = True
            if finished:
                break
            K = K+1

    return m


for K in range(T):
    N = int(input())
    r = f(N)
    print("Case #" + str(K+1)+ ": " + str(r))
