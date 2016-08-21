import sys

def count_sheep(n):
    if n == 0:
        return 'INSOMNIA'

    digits = set(map(str, range(10)))
    i = 1
    while len(digits) > 0:
        digits -= set(str(n*i))
        i += 1
    return n*(i-1)

num_tests = int(sys.stdin.readline().strip())
for i in range(num_tests):
    N = int(sys.stdin.readline().strip())
    print 'Case #%d:' % (i+1), count_sheep(N)
