def solve(num):
    if num == 0:
        return 'INSOMNIA'

    d = set()
    n, m = num, 1
    while len(d) < 10:
        n = num * m
        d.update(set(str(n)))
        m += 1

    return n

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        num = int(raw_input())
        print 'Case #{}: {}'.format(i + 1, solve(num))
