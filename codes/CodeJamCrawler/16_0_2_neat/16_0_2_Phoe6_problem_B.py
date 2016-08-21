import sys

def read_number_of_test_cases(fobject=None):
    if fobject:
        T = int(fobject.readline())
    else:
        T = int(raw_input())
    return T


def read_test_case(fobject=None):
    if fobject:
        TC = fobject.readline()
    else:
        TC = raw_input()
    return TC.strip()


def solve_test_case(S):
    assert isinstance(S, str)
    reversed_string = S[::-1]
    count = 0
    for idx, char in enumerate(reversed_string):
        if idx == 0:
            if char == '-':
                count += 1
        else:
            if char != reversed_string[idx-1]:  # previous character
                count += 1
    return count


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


