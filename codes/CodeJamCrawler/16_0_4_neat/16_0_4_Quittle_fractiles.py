import itertools
import math
import sys

IMPOSSIBLE = 'IMPOSSIBLE'

def main():
    num_cases = int(sys.stdin.readline())

    line_num = 1
    for line in sys.stdin:
        line = line.strip()

        original_length, complexity, students = (int(n) for n in line.split(' '))

        tiles = compute(original_length, complexity, students)
        solution = None
        if tiles is None:
            solution = IMPOSSIBLE
        else:
            assert_is_numeric_list(tiles)
            solution = ' '.join(map(lambda t: str(t + 1), tiles))
        assert_is_string(solution)

        print 'Case #%d: %s' % (line_num, solution)

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
    generate_test()
    stringify_test()


def compute(original_length, complexity, students):
    ''' Builds a list of tiles to check for gold to guarantee found gold or None if not possible '''
    assert_is_numeric(original_length)
    assert_is_numeric(complexity)
    assert_is_numeric(students)

    if students < original_length:
        return None

    ret = []
    i = 0
    for index in generate_next_item(original_length, complexity - 1):
        if i == students:
            break

        assert index is not None
        #print index,
        ret.append(index)
        i += 1

    return ret

#   LG
# LG/\GG

def generate_next_item(original_length, complexity):
    ''' Generator for indices guaranteed to be unique from the original '''
    amt = 0 if complexity == 0 else original_length ** complexity
    for i in xrange(original_length):
        yield i * (amt) + i
        #yield original_length * complexity ** 2 * i + i

    yield None


def generate(k, c):
    ''' Generates the the result given starting sequence k and complexity c '''
    assert_is_bool_list(k)
    assert_is_numeric(c)
    assert c >= 1

    gold_section = [True] * len(k)
    assert len(gold_section) == len(k)

    ret = k
    for i in xrange(1, c):
        tmp = []
        for p in ret:
            tmp += gold_section if p else k
        ret = tmp
    return ret


def generate_test():
    assert [] == generate([], 1)
    assert [True] == generate([True], 1)
    assert [True] == generate([True], 2)
    assert [True, True, True, True] == generate([True, True], 2)
    assert [True, True, True, False] == generate([True, False], 2)
    assert [False, True, False] == generate([False, True, False], 1)
    assert [False, True, False,
            True, True, True,
            False, True, False] == generate([False, True, False], 2)
    assert [False, True, False,
            True, True, True,
            False, True, False,
            True, True, True,
            True, True, True,
            True, True, True,
            False, True, False,
            True, True, True,
            False, True, False] == generate([False, True, False], 3)


def preprocess():
    ''' For generating data to visualize fractiles '''
    origin_len = 2
    complexity = 3
    for combination in itertools.product([True, False], repeat=origin_len):
        print stringify(generate(combination, complexity))

    indices_of_note = set([0, 5])
    for i in xrange(origin_len ** complexity):
        sys.stdout.write('^' if i in indices_of_note else ' ')
    print


def stringify(bool_list):
    ''' Converts a boolean list into a string of gold (True) and lead (False) '''
    assert_is_bool_list(bool_list)

    return reduce(lambda prev, b: prev + ('G' if b else 'L'), bool_list, '')


def stringify_test():
    assert '' == stringify([])
    assert 'G' == stringify([True])
    assert 'L' == stringify([False])
    assert 'GL' == stringify([True, False])
    assert 'LGL' == stringify([False, True, False])


if __name__ == '__main__':
    test()
    #print 'All tests passed'
    #preprocess()
    main()