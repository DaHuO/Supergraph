"""

"""

import sys


if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        n_test_cases = int(f.readline())
        test_cases = []

        for i in range(n_test_cases):
            test_cases.append(tuple(map(int, f.readline().split(' '))))

    solutions = []
    for K, C, S in test_cases:
        # K == S is always possible
        solutions.append(range(1, K + 1))

    with open('fractiles-small.txt', 'w') as f:
        n = 1
        s_lst = []
        for solution in solutions:
            s_lst.append("Case #%d: %s" % (n, ' '.join(map(str, solution))))
            n += 1

        f.write('\n'.join(s_lst))
