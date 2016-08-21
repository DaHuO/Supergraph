"""Code jam Revenge of the Pancakes."""

import fileinput

for case, stack in enumerate(fileinput.input()):
    if case == 0:
        continue

    stack = stack.strip()
    n_blocks = 0
    prev = None

    for p in stack:
        if p == prev:
            continue
        else:
            n_blocks += 1
            prev = p

    if stack[-1] == '-':
        print('Case #{}: {}'.format(case, n_blocks))
    else:
        print('Case #{}: {}'.format(case, n_blocks-1))
