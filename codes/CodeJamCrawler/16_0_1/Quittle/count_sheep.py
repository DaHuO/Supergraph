import sys

def main():
    num_cases = int(sys.stdin.readline())

    line_num = 1
    for line in sys.stdin:
        result = compute(int(line))
        assert_is_numeric(result)
        assert result >= -1
        result = 'INSOMNIA' if result == -1 else str(result)

        print 'Case #%d: %s' % (line_num, result)
        line_num += 1

    assert num_cases == line_num - 1

def assert_is_numeric(n):
    assert type(n) in [int, long]


def test():
    count_digits_test()
    all_digits_found_test()


def find_digits(n):
    assert_is_numeric(n)

    return set(int(digit) for digit in str(n))


def count_digits_test():
    assert set([0]) == find_digits(0)

    assert set([0, 1]) == find_digits(100)

    assert set([0]) == find_digits(00)

    assert set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == find_digits(12345678901234567890)


def compute(n):
    assert_is_numeric(n)

    if n == 0:
        return -1

    digits = set()
    i = 0
    while not all_digits_found(digits):
        i += 1
        digits = digits.union(find_digits(n * i))

        # Safety check for large numbers
        if i > 10000000:
            return -1

    return n * i


def all_digits_found(digits):
    assert type(digits) is set
    assert len(digits) >= 0 and len(digits) <= 10

    return len(digits) == 10


def all_digits_found_test():
    assert False == all_digits_found(set())

    assert False == all_digits_found(set([0]))

    assert False == all_digits_found(set([0, 2, 3, 4, 5, 6, 7, 8, 9]))

    assert True == all_digits_found(set(xrange(10)))


if __name__ == '__main__':
    test()
    #print 'All tests passed'
    main()