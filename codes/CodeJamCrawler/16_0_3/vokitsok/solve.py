import sys
import re
import itertools


def find_devisor(n):
    i = 2
    while i * i <= n and i < 1000:
        if n % i == 0:
            return i
        i += 1
    return None


def handle_case(case_num):
    N, J = map(int, sys.stdin.readline().strip().split())
    print 'Case #{0}:'.format(case_num)

    found = 0

    for val in xrange(2 ** (N - 2)):
        candidate = '1' + '{{0:0{0}b}}'.format(N - 2).format(val) + '1'

        devisors = []
        good = True
        for base in range(2, 11):
            num = int(candidate, base)
            devisor = find_devisor(num)
            if devisor is None:
                good = False
                break
            devisors.append(devisor)
        if good:
            print "{0} {1}".format(candidate, ' '.join(map(str, devisors)))
            found += 1
            if found == J:
                return


def main():
    T = int(sys.stdin.readline().strip())
    for case_num in xrange(1, T+1):
        handle_case(case_num)


if __name__ == '__main__':
    main()