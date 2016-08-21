import sys

def main():
    num_cases = int(sys.stdin.readline())

    line_num = 1
    for line in sys.stdin:
        line = line.strip()
        flips = compute(line)
        assert_is_numeric(flips)
        assert flips >= 0 and flips <= len(line)

        print 'Case #%d: %d' % (line_num, flips)
        line_num += 1

    assert num_cases == line_num - 1


def assert_is_numeric(n):
    assert type(n) in [int, long]


def assert_is_bool_list(arr):
    for v in arr:
        assert type(v) is bool


def test():
    make_bool_list_test()
    recurse_count_flips_test()

def compute(pancakes):
    for pancake in pancakes:
        assert pancake in '+-'

    bool_pancakes = make_bool_list(pancakes)
    assert_is_bool_list(bool_pancakes)

    return recurse_count_flips(bool_pancakes)

def make_bool_list(arr):
    ''' Converts a list of '+' and '-' into a list booleans with True for '+' and False for '-' '''
    for v in arr:
        assert v in '+-'
    return [v == '+' for v in arr]

def make_bool_list_test():
    assert [] == make_bool_list('')
    assert [True] == make_bool_list('+')
    assert [False] == make_bool_list('-')
    assert [True, False, True, False] == make_bool_list('+-+-')


def recurse_count_flips(arr):
    '''
        Counts the number of times the array flips from True to False, except for the last flip if
        it is to a positive.
    '''
    assert_is_bool_list(arr)

    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 0 if arr[0] else 1 # No need to flip if smiley at the end
    else:
        ret = 0 if arr[0] == arr[1] else 1
        return ret + recurse_count_flips(arr[1:])

def recurse_count_flips_test():
    assert 0 == recurse_count_flips([])
    assert 0 == recurse_count_flips([True])
    assert 0 == recurse_count_flips([True, True])
    assert 1 == recurse_count_flips([False])
    assert 1 == recurse_count_flips([False, False])
    assert 1 == recurse_count_flips([False, True])
    assert 2 == recurse_count_flips([True, False])
    assert 2 == recurse_count_flips([True, False, True])
    assert 2 == recurse_count_flips([True, False, False])
    assert 2 == recurse_count_flips([True, False, False, True, True])
    assert 4 == recurse_count_flips([True, False, False, True, False])

if __name__ == '__main__':
    test()
    #print 'All tests passed'
    main()