def diff_digits(v1, v2):
    for i in range(10):
        if v1[i] != v2[i]:
            return True

    return False


def found_solution(v, m):
    return sum(1 for i in v if i) == 10


def solve(n):
    v = [0] * 10
    current_multipler = 1
    while not found_solution(v, n * current_multipler):
        old_v = v[:]

        ith_n = n * current_multipler
        while ith_n != 0:
            c = ith_n % 10
            ith_n /= 10
            v[c] += 1

        if not diff_digits(v, old_v):
            return "INSOMNIA"

        current_multipler += 1

    return str(n * (current_multipler - 1))


def read_input_data():
    no_of_test_cases = int(raw_input())
    for i in xrange(1, no_of_test_cases + 1):
        solution = solve(int(raw_input()))
        print "Case #%d: %s" % (i, solution)


read_input_data()
