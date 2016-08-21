import random
from sympy.ntheory.factor_ import pollard_rho

def read_int():
    return int(raw_input())


def read_int_list():
    return [int(x) for x in raw_input().split()]


def number_in_base(x, base, N):
    number = 1 + base**(N-1)
    for i in range(0, N-2):
        if (x & (1 << i)) > 0:
            number += base ** (1+i)
    return number


def is_coinjam(x, N):
    factors = []
    for base in range(2, 11):
        number = number_in_base(x, base, N)
        c = pollard_rho(number, max_steps=1000)
        if c == number or c is None:
            return None
        factors.append(c)
    return factors


def solve():
    N, J = read_int_list()
    i = 0
    format_str = "1{0:0%db}1" % (N-2)
    used = {}
    while J > 0:
    # while i < 2**(N-2):
        i = random.randint(0, 2**(N-2))
        if i in used:
            continue
        used[i] = True
        factors = is_coinjam(i, N)
        if factors:
            print format_str.format(i) + " " + " ".join(str(x) for x in factors)
            J -= 1
            if J == 0:
                return
        i += 1


def main():
    T = read_int()
    for i in range(T):
        print 'Case #%d:' % (i+1)
        solve()

if __name__ == '__main__':
    main()
