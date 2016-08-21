def calculate(N):
    if N == 0:
        return 'INSOMNIA'
    l = []
    n = N
    i = 2
    while n <= 10 ** 6:
        s = str(n)
        for elem in s:
            if elem not in l:
                l.append(elem)
        if len(l) == 10:
            return n
        n = i * N
        i += 1

    return 'INSOMNIA'
