
def f(x, d):
    while x > 0:
        c = x % 10
        x = x // 10
        d[c] = 1


input_file = open('A-large.in', 'r')
out_file = open('A-res-large.out', 'w')

test_cases = int(input_file.readline())

for t in range(1, test_cases + 1):
    n = int(input_file.readline())

    if n == 0:
        out_file.write('Case #%d: INSOMNIA\n' % t)
        continue

    iter = 1
    d= {}
    while len(d) < 10:
        f(iter * n, d)
        iter += 1

    iter -= 1

    out_file.write('Case #{:d}: {:d}\n'.format(t, iter * n))

