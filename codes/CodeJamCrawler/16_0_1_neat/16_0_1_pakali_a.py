import sys

def is_sleep(n, digits):
    return len(digits)==10

def counting_sheep(n, test_case):
    if n == 0:
        print "Case #%d: INSOMNIA" % (test_case)
        return

    n_orginal = n
    digits = []

    i = 0

    while True:
        list_of_digits = str(n)

        for digit in list_of_digits:
            digits.append(digit)
        digits = list(set(digits))

        if is_sleep(n, digits):
            print "Case #%d: %s" % (test_case, n)
            break
        else:
            i += 1
            n = n_orginal * i

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        s = f.readline().split()
        c = int(s[0])

        counting_sheep(c, _t+1)