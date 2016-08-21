import fileinput

lines = list(fileinput.input())


def solve(stack):
    if stack == ['-']:
        return 1
    elif stack == ['+']:
        return 0

    flips = 0
    head = stack[0]

    while True:
        try:
            other_i = stack.index(rev(head))
            stack = [rev(e) for e in stack[:other_i]] + stack[other_i:]
            flips += 1
            head = stack[0]
        except Exception:
            break
    if stack[-1] == '-':
        flips += 1

    return flips


def rev(elem):
    return '+' if elem == '-' else '-'

for case, line in enumerate(lines[1:], 1):
    stack = list(line.strip())
    flips = solve(stack)
    print('Case #{}: {}'.format(case, flips))
