"""

"""

import sys


if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        n_test_cases = int(f.readline())
        test_cases = []

        for i in range(n_test_cases):
            test_cases.append(f.readline()[:-1])

    solutions = []
    for s in test_cases:
        n = 0
        s += '+'
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                n += 1

        solutions.append(n)

    with open('pancakes-large.txt', 'w') as f:
        n = 1
        s_lst = []
        for solution in solutions:
            s_lst.append("Case #%d: %d" % (n, solution))
            n += 1

        f.write('\n'.join(s_lst))
