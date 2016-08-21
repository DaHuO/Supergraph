import re

def solve_case(case):
    if '-' not in case:
        return 0

    if '+' not in case:
        return 1

    flips = 0 if case[0] == '+' else 1

    subbed = re.sub(r'\++', '|', case)

    segments = subbed.split('|')
    segments.pop(0)

    if segments[-1] == '':
        segments.pop(-1)

    return (len(segments) * 2) + flips

def parse(input_lines):
    n_cases = int(input_lines.pop(0))
    cases = []

    for i in range(len(input_lines)):
        cases.append(input_lines[i])

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
    solve('B-large')
    print('Done!')