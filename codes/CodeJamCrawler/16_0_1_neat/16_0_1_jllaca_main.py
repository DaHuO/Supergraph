def f(n):
    digits = set()
    multiples = set()
    i, m = 1, n
    while True:
        if m in multiples:
            break
        multiples.add(m)
        for digit in [int(c) for c in str(m)]:
            digits.add(digit)
        if len(digits) == 10:
            return m
        m += n
        i += 1
    return -1

t = input()
for i in range(t):
    n = input()
    m = f(n)
    print 'Case #{}: {}'.format(i + 1, m if m > 0 else 'INSOMNIA')
