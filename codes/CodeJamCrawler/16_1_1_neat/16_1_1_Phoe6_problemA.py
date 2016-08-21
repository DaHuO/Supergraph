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
    all_chars = list(S)
    last_word = []
    for each_char in all_chars:
        if len(last_word) == 0:
            last_word.append(each_char)
            continue
        if each_char >= last_word[0]:
            last_word.insert(0, each_char)
        else:
            last_word.append(each_char)

    return "".join(last_word)


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
