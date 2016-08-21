def f(n):
    if n == 0:
        return 'INSOMNIA'

    seen = set()
    i = 1
    while True:
        for j in str(i*n):
            seen.add(j)
        if len(seen) == 10:
            return str(i*n)
        i += 1

t = int(input())
for i in range(t):
    n = int(input())
    print('Case #%d: %s'%(i+1, f(n)))
