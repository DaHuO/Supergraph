import sys


def read_input(filename, operation=lambda x: x):
    with open(filename, 'r') as f:
        return (operation(item) for item in f.readlines())


def write_results(results, filename):
    with open(filename, 'w') as f:
        f.writelines(results)


def to_booleans(stack):
    return [item == '+' for item in stack]


def flip(stack, index):
    i = 0
    while i < index:
        stack[i] = not stack[i]
        i += 1


def get_next_flip(stack, start=0):
    side = stack[start]
    try:
        return stack.index(not side, start)
    except ValueError:
        return len(stack)


def orient_stack(stack):
    stack = to_booleans(stack)
    flips = 0
    while not all(stack):
        flip_at = get_next_flip(stack)
        flip(stack, flip_at)
        flips += 1
    return flips


# get script name
name = sys.argv[0].split('/').pop().split('.')[0]

# read trials from script input file and strip each line
trials = read_input('{}.in'.format(name), lambda x: x.rstrip())

# first line is number of trials, which isn't needed
next(trials)

# run trials and collect results
data = (orient_stack(trial) for trial in trials)

# create output strings from results
output = ('Case #{}: {}\n'.format(i + 1, result) for i, result in enumerate(data))

# write output
write_results(output, '{}.out'.format(name))
