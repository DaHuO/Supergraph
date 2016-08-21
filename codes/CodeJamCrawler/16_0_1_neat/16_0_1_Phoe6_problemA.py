import sys

def read_number_of_test_cases(fobject=None):
    if fobject:
        T = int(fobject.readline())
    else:
        T = int(raw_input())
    return T


def read_test_case(fobject=None):
    if fobject:
        TC = int(fobject.readline())
    else:
        TC = int(raw_input())
    return TC


def solve_test_case(N):
    seen_so_far = []
    counter = 1
    next_num = counter * N
    likes_to_see = set(range(10))

    while True:
        if len(likes_to_see) == 0:
            return seen_so_far[-1]

        digits = map(int, list(str(next_num)))
        for digit in digits:
            likes_to_see.discard(digit)

        seen_so_far.append(next_num)

        counter += 1
        next_num = counter * N
        if next_num in seen_so_far:
            return "INSOMNIA"

def solve_it(num_test_cases, fobject=None):
    for tc in range(num_test_cases):
        test_case = read_test_case(fobject=fobject)
        result = solve_test_case(test_case)
        print "Case #{testcase}: {result}".format(testcase=tc+1, result=result)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_case_file = sys.argv[1]
        with open(test_case_file) as fobj:
            num_test_cases = read_number_of_test_cases(fobj)
            solve_it(num_test_cases, fobj)
    else:
        num_test_cases = read_number_of_test_cases()
        solve_it(num_test_cases)


