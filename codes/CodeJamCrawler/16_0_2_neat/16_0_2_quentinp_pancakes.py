import sys

def minimal_actions(stack):
    # Let's first eliminate all + at the bottom of the stack
    while len(stack) > 0 and stack[-1] == '+':
        stack = stack[:-1]

    if len(stack) == 0:
        return 0

    actions = 1
    before = stack[0]
    for i in range(1, len(stack)):
        if stack[i] != before:
            before = stack[i]
            actions += 1

    return actions

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue

    stack = line.strip()
    n = minimal_actions(stack)
    print('Case #{}: {}'.format(i, n))

