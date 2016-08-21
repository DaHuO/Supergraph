
def solve_case(case):
    if case == '0':
        return 'INSOMNIA'

    unseen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    next_ctr = 1
    last_num = int(case)

    while unseen:
        curr_num = next_ctr * int(case)

        digits = str(curr_num)
        for d in digits:
            if d in unseen:
                unseen.remove(d)

        next_ctr += 1
        last_num = curr_num

    return last_num

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
    solve('A-large')
    print('Done!')
