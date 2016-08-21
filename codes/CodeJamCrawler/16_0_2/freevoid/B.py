import sys

def collapse(pancakes):
    start = pancakes[0]
    rank = 1
    current = start
    for p in pancakes:
        if p != current:
            current = p
            rank += 1

    return (rank, start)


def get_solutions(S):
    solutions = {
        (1, '+'): 0,
        (1, '-'): 1
    }

    for rank in range(2, S + 1):
        if rank % 2 == 1:
            solutions[(rank, '+')] = \
                1 + min(solutions[(rank - 1, '-')],
                    1 + solutions[(rank - 1, '+')])
            solutions[(rank, '-')] = \
                1 + min(solutions[(rank - 1, '+')],
                    1 + solutions[(rank - 1, '-')])
        else:
            solutions[(rank, '+')] = \
                1 + solutions[(rank - 1, '-')]
            solutions[(rank, '-')] = \
                1 + solutions[(rank - 1, '+')]

    return solutions

_solutions = get_solutions(100)

def solve(pancakes):
    return _solutions[collapse(pancakes)]

def read_int(fp):
    return int(fp.readline())

if __name__ == '__main__':
    T = read_int(sys.stdin)
    for i in range(T):
        print 'Case #%d: %s' % (i + 1, solve(sys.stdin.readline().strip()))
