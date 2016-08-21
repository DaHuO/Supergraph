def g(n):
    v = 0
    while n:
        v |= 1 << (n % 10)
        n //= 10
    return v
def f(n):
    if n == 0:
        return 'INSOMNIA'
    c, d = n, g(n)
    while d != 1023:
        c += n
        d |= g(c)
    return c
for t in range(int(input())):
    print('Case #{}: {}'.format(t + 1, f(int(input()))))
