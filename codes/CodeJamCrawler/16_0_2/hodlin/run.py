from itertools import filterfalse
FILENAME = 'B-large'


def optimal_choises(stack):
    stack = list(map(lambda x: x == '+', stack))
    # print(stack)
    changes = 0
    while len(list(filterfalse(lambda x: x, stack))):
        changes += 1
        if len(stack) == len(list(filterfalse(lambda x: x, stack))):
            stack[:] = list(map(lambda x: not x, stack[:][::-1]))
            # print(stack)
            return changes
        same_pancakes = 1
        while stack[same_pancakes] == stack[0]:
            same_pancakes += 1
        stack[:same_pancakes] = list(map(lambda x: not x, stack[:same_pancakes][::-1]))
        # print(stack)
        # print(list(map(lambda x: not x, stack[:same_pancakes][::-1])))
        # break

    return changes

with open('{}.in'.format(FILENAME), 'r') as f:
    input = f.read().split()

with open('{}.out'.format(FILENAME), 'w') as f:
    for test_case in range(1, int(input[0]) + 1):
        out = optimal_choises(input[test_case])
        f.write('Case #{num}: {value}\n'.format(num=test_case, value=out))
