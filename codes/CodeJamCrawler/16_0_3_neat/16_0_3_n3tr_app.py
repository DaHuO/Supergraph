
import math

def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True





def generate_binary(length, max):

    J = 1

    mid_length = length - 2
    min_value = 0
    max_value = int('1' * mid_length, 2)

    for i in range(min_value, max_value+1):
        n = "{0:b}".format(i)
        if len(n) < mid_length:
            n = '0' * (mid_length - len(n)) + n
        n = '1' + n + '1'

        prime = False
        for i in xrange(2, 11):
            v = int(n, i)
            d = ''
            if is_prime(v):
                prime = True
                break

        if not prime:
            t = []
            for i in xrange(2, 11):
                v = int(n, i)
                for d in xrange(2, v / 2):
                    if v % d == 0:
                        t.append(str(d))
                        break

            print '{} {}'.format(n, ' '.join(t))

            J += 1
            if J > max:
                return



def read_file():
    f = open('C-small.in', 'r')
    return f.read().splitlines()


lines = read_file()
t = int(lines[0])  # read a line with a single integer
for i in xrange(1, t + 1):
    N, J = lines[i].split(' ')
    print "Case #{}:".format(i)
    generate_binary(int(N), int(J))
