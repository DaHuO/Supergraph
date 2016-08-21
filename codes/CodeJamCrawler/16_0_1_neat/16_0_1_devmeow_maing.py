INPUT = 'input.txt'
OUTPUT = 'output.txt'


def int2digits(x):
    res = set()
    while x:
        res.add(x % 10)
        x //= 10
    return res

with open(INPUT, 'r') as f:
    with open(OUTPUT, 'w') as g:
        t = int(f.readline())
        for i in range(t):
            d = set()
            g.write('Case #{}: '.format(i + 1))
            n = int(f.readline())
            if n == 0:
                g.write('INSOMNIA')
            else:
                i = 2
                k = n
                while True:
                    d.update(int2digits(k))
                    if len(d) == 10:
                        g.write('{}'.format(k))
                        break
                    k = n * i
                    i += 1
            g.write('\n')
