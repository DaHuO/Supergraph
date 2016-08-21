"""
__author__ = 'samvitello'
codejam qualifiying counting sheep
input: stdin, number of T test cases and T ints n
output: the number of iterations i, until the digits
    that make up n * i + 1 = set(0,1,2,3,4,5,6,7,8,9)
"""


def max_num_for_all_digits(n):
    """takes int n
    returns number of iterations i until n*i+1 have produced all 10 digits
    """
    seen_set = set()
    new_num = 0

    while len(seen_set) < 10:
        new_num += n
        for digit in str(new_num):
            seen_set.add(digit)

    return new_num


def print_answer(answer_list):
    for t, num in enumerate(answer_list):
        print "Case #" + str(t+1) + ": " + str(num)


if __name__ == "__main__":
    iterations = int(raw_input())
    total_iter = []

    for i in xrange(iterations):
        test_case = int(raw_input())
        if test_case == 0:
            total_iter.append("INSOMNIA")
            continue
        total_iter.append(max_num_for_all_digits(test_case))

    print_answer(total_iter)



