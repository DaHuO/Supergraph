def test():
    N = int(input())
    if N == 0:
        return -1

    d = {}
    i = 0
    while len(d) < 10:
        i+=1
        t = N*i
        for c in str(t):
            if not c in d:
                d[c] = 1
    return i*N


T = int(input())

for i in range(T):
    a = test()
    print('Case #'+str(i + 1)+': '+(str(a) if a > 0 else 'INSOMNIA'))
