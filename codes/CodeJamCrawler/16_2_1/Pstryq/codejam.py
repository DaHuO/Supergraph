__author__ = 'Patryk'


def read_single():
    return int(raw_input().strip())


def read_int_line():
    return map(int, raw_input().strip().split())


def read_string():
    return raw_input().strip()


def print_solution(solution_number, solution):
    print 'Case #{}: {}'.format(solution_number, solution)


def red(result, counts, char, check, full):
    if counts.get(check, 0) > 0:
        v = counts.get(check, 0)
        for k in full:
            counts[k] -= v
        result += char * v
    return result, counts


def solution():
    s = list(read_string())
    counts = {char: s.count(char) for char in s}
    result = ''

    digs = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    result, counts = red(result, counts, '0', 'Z', 'ZERO')
    result, counts = red(result, counts, '6', 'X', 'SIX')
    result, counts = red(result, counts, '4', 'U', 'FOUR')
    result, counts = red(result, counts, '5', 'F', 'FIVE')
    result, counts = red(result, counts, '7', 'V', 'SEVEN')
    result, counts = red(result, counts, '2', 'W', 'TWO')
    result, counts = red(result, counts, '3', 'R', 'THREE')
    result, counts = red(result, counts, '8', 'G', 'EIGHT')
    result, counts = red(result, counts, '1', 'O', 'ONE')
    result, counts = red(result, counts, '9', 'I', 'NINE')
    return ''.join(sorted(result))


t = read_single()
for i in xrange(1, t + 1):
    print_solution(i, solution())
