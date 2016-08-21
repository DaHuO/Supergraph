__author__ = 'fdoherty'


def output(case, data):
    print 'Case #%s:' % case, data

def get_digits(value):
    return set(str(value))


def solve(case_num, start_num):
    all_digits = set()
    x = start_num
    iterations = 0
    while iterations < 100:
        digits = get_digits(x)
        all_digits = all_digits.union(digits)
        if len(all_digits) == 10:
            output(case_num, x)
            return
        x += start_num
        iterations += 1
    output(case_num, 'INSOMNIA')


NUM_CASES = input()
for test_num in range(NUM_CASES):
    start_num = raw_input()
    solve(test_num+1, int(start_num))