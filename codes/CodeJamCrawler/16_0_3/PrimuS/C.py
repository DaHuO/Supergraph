# library available at https://pypi.python.org/pypi/primefac
import primefac

def f(s, e):
    while s < e:
        if s % 2 == 0:
            s += 1
            continue

        st = '{0:b}'.format(s)
        ll = []
        for b in range(2, 11):
            cur = int(st, b)
            if primefac.isprime(cur):
                break
            ll.append(cur)
        else:
            for i in xrange(len(ll)):
                ll[i] = primefac.primefac(ll[i]).next()

            return (s, ll)

        s += 1

# f(9, 10)
# exit(0)

input_file = open('C-small-attempt0 (1).in', 'r')
out_file = open('C-res.out', 'w')

test_cases = int(input_file.readline())


for t in range(1, test_cases + 1):
    n, j = (int(x) for x in input_file.readline().split())

    out_file.write('Case #%d:\n' % t)

    first = (1 << (n - 1)) + 1
    last = (1 << n)

    for k in range(j):
        res = f(first, last)
        first = res[0] + 1

        out_file.write('{0:b}'.format(res[0]))
        for x in res[1]:
            out_file.write(' {0:d}'.format(x))
        out_file.write('\n')