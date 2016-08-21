import itertools
import math
import sys

def main():
    num_cases = int(sys.stdin.readline())

    line_num = 1
    while True:
        line = sys.stdin.readline()
        if not line:
            break

        line = line.strip()

        num_kids = int(line)

        bffs = [int(n) for n in sys.stdin.readline().strip().split(' ')]
        assert num_kids == len(bffs)
        assert_is_numeric_list(bffs)

        solution = compute(bffs)
        assert_is_numeric(solution)
        assert solution <= num_kids

        print 'Case #%d: %d' % (line_num, solution)

        line_num += 1

    assert num_cases == line_num - 1


def assert_is_numeric(n):
    assert type(n) in [int, long]


def assert_is_string(s):
    assert isinstance(s, basestring)


def assert_is_numeric_list(arr):
    for n in arr:
        assert_is_numeric(n)


def assert_is_bool_list(arr):
    for b in arr:
        assert type(b) is bool


def test():
    pass


def compute(bffs):
    ''' ??? '''

    num_kids = len(bffs)
    kid_ids = range(1, num_kids + 1)

    for circle_size in xrange(num_kids, 0, -1):
        #print 'trying circle of size %d' % circle_size
        for circle in itertools.permutations(kid_ids, circle_size):
            if is_valid_circle(circle, bffs):
                #print circle
                sys.stdout.flush()
                return circle_size

    return 0


def is_valid_circle(circle, bffs):
    circle_size = len(circle)
    assert circle_size <= len(bffs)

    if circle_size <= 1:
        return True

    for i in xrange(circle_size):
        kid_id = circle[i]
        bff_id = bffs[kid_id - 1]

        left_id = circle[i - 1]
        right_index = i + 1
        right_id = circle[0] if right_index == circle_size else circle[right_index]

        if left_id != bff_id and right_id != bff_id:
            return False

    return True


if __name__ == '__main__':
    test()
    #print 'All tests passed'
    main()