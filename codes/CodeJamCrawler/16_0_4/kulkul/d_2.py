import itertools
from math import sqrt;
from itertools import count, islice


def find_solution(K, C, S):
    if S < K:
        return [-1]
    base = [i for i in range(K)]
    # print(base)
    base_len = K
    for c in range(C - 1):
        base = [i * base_len for i in base]
        base = [x + y for x, y in zip(base , range(base_len))]
        # print(base)
    return [i + 1 for i in base]

def test():
    print("start test")
    test_cases = [
        [[2, 3, 2], [1, 8]],
        [[1, 1, 1], [1]],
        [[2, 1, 1], [-1]],
        [[2, 1, 2], [1, 2]],
        [[3, 2, 3], [1, 5, 9]],
        [[10, 2, 10], [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]]
    ]
    solution = []
    try:
        for test_case in test_cases:
            solution = find_solution(test_case[0][0], test_case[0][1], test_case[0][2])
            assert solution == test_case[1]
            print("pass")
    except Exception as e:
        print("fail")
        print(test_case[0][0], test_case[0][1], test_case[0][2], test_case[1], solution)
        raise e

    print("end test")


test()

f = open('output.txt', 'w')

t = int(input())

for i in range(t):
    input_numbers = [int(x) for x in input().split(' ')]
    K = input_numbers[0]
    C = input_numbers[1]
    S = input_numbers[2]

    solution = find_solution(K, C, S)

    output_str = "Case #%d: %s" % (i + 1, solution == [-1] and "IMPOSSIBLE" or ' '.join([str(x) for x in solution]))
    print(output_str)
    f.write(output_str + "\n")
