__author__ = 'Patryk'

def read_single():
    return int(raw_input().strip())

def read_line():
    return map(int, raw_input().strip().split())

def read_string():
    return raw_input().strip()

def print_solution(solution_number, solution):
    print 'Case #{}: {}'.format(solution_number, solution)

def solution():
    S = read_string()
    result = ''
    for letter in S:
        if len(result) == 0:
            result += letter
        else:
            if letter >= result[0]:
                result = letter + result
            else:
                result += letter
    return result

t = read_single()
for i in xrange(1, t + 1):
    print_solution(i, solution())
