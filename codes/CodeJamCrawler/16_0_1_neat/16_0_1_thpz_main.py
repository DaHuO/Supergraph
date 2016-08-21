fn = 'A-large'

in_f = file(fn + '.in', 'r')
out_f = file(fn + '.out', 'w')

t = int(in_f.readline())

for i in range(1, t + 1):
    n = int(in_f.readline())

    if n == 0:
        out_f.write('Case #{}: {}\n'.format(i, 'INSOMNIA'))
        continue

    j = 0
    digits = [str(d) for d in range(10)]
    while digits:
        j += 1
        x = n * j
        while x:
            d = str(x % 10)
            if d in digits:
                digits.remove(d)
            x //= 10

    out_f.write('Case #{}: {}\n'.format(i, n * j))
