import sys

T = int(sys.stdin.readline())
for t in xrange(1, T + 1):
    n = int(sys.stdin.readline())

    if n == 0:
        sys.stdout.write('Case #%d: INSOMNIA\n' % t)
        continue

    seen_digits = [False for i in xrange(10)]
    x = 0

    while not all(seen_digits):
        x += n
        for digit in str(x):
            seen_digits[int(digit)] = True

    sys.stdout.write('Case #%d: %d\n' % (t, x))
