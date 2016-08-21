T = int(input())
for t in range(T):
    N = int(input())
    if N == 0:
        r = 'INSOMNIA'
    else:
        digits = set(str(N))
        k = 1
        c = N
        while len(digits) < 10:
            c += N
            k += 1
            digits.update(str(c))
        r = str(c)
    print('Case #%d: %s' % (t + 1, r))
