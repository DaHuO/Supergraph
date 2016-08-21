def a(x):
    if x==0: return 'INSOMNIA'
    n = 10
    digits = [False for i in range(10)]
    i = 1
    while n > 0:
        a = x*i
        while a != 0:
            dig = a % 10
            if not digits[dig]:
                n -= 1
                digits[dig] = True
            a //= 10
        i += 1
    return x*(i-1)

cache = {}
with open('A-large.in') as f:
    with open('output.txt', 'w') as g:
        n = int(f.readline())
        for i in range(n):
            x = int(f.readline())
            if x not in cache:
                cache[x] = a(x)
            g.write('Case #{}: {}\n'.format((i+1), cache[x]))
