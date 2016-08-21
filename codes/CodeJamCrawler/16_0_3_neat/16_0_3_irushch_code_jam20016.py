# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

from itertools import product


def bases(n):
    return [int(n, i) for i in xrange(2, 11)]


def find_division(n):
    for x in xrange(2, 3000):
        if n % x == 0:
            return x


if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        print 'Case #{}:'.format(i)
        # read a list of integers
        n, j = [int(x) for x in raw_input().split(' ')]

        printed = 0
        for num in product(['1', '0'], repeat=n):
            num = ''.join(num)
            if num[0] != '1' or num[-1] != '1':
                continue
            num_bases = bases(num)
            divisions = []
            for base in num_bases:
                divis = find_division(base)
                if not divis:
                    divisions = []
                    break
                divisions.append(str(divis))

            if divisions and printed < j:
                print "{} {}".format(num, ' '.join(divisions))
                printed += 1

            if printed >= j:
                break
