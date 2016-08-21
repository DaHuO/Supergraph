"""

"""

import sys, copy


def test(counter, n):

    for k in str(n):
        counter[k] += 1

    return all([count > 0 for _, count in counter.items()])


if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        n_test_cases = int(f.readline())
        test_cases = []

        for i in range(n_test_cases):
            test_cases.append(int(f.readline()))

    solutions = []
    for N in test_cases:
        if N == 0:
            solutions.append(-1)
            continue
        else:
            i = 1
            n = N
            counter = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
            while not test(counter, n):
                i += 1
                n = i * N

            solutions.append(n)

    with open('beatrix-large.txt', 'w') as f:
        n = 1
        s_lst = []
        for solution in solutions:
            s_lst.append("Case #%d: %s" % (n, str(solution) if solution >= 0 else 'INSOMNIA'))
            n += 1

        f.write('\n'.join(s_lst))
