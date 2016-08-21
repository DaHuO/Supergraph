
def solve_case(case):
    k, c, s = case

    parts = k**c / k

    return ' '.join([str(i * parts) for i in range(1, k + 1)])

def parse(input_lines):
    n_cases = int(input_lines.pop(0))
    cases = []

    for i in range(len(input_lines)):
        cases.append([int(i) for i in input_lines[i].split(' ')])

    return n_cases, cases

def solve(input_file):
    with open(input_file + '.in', 'r') as f:
        input_lines = f.read().split('\n')

    n_cases, cases = parse(input_lines)

    solution = []
    for i in range(0, n_cases):
        answer = solve_case(cases[i])
        solution.append('Case #%s: %s' % (i + 1, answer))

    with open(input_file + '.out', 'w') as f:
        f.write('\n'.join(solution))

if __name__ == '__main__':
    # solve('sample')
    solve('D-small-attempt0')
    print('Done!')

