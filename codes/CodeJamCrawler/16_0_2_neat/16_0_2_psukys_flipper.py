import sys

def read_input(file):
    inputs = open(file).read().strip().split('\n')[1:]
    # small hack, since I've understood the pancake ordering wrong
    inputs = [s[::-1] for s in inputs]
    return inputs

def flip(stack, idx):
    # Strings are immutable in python
    new_stack = stack[:idx]
    for i in xrange(idx, len(stack)):
        if stack[i] == '-':
            new_stack = new_stack + '+'
        else:
            new_stack = new_stack + '-'
    return new_stack

def get_happy(stack):
    # Flip from left to right
    print("NEW STACK", stack)
    flips = 0
    for i in xrange(len(stack)):
        print(stack)
        if stack[i] == '-':
            flips = flips + 1
            stack = flip(stack, i)

    return flips


if __name__ == '__main__':
    inputs = read_input(sys.argv[1])
    counter = 1
    output = []
    for i in inputs:
        output.append("Case #{0}: {1}".format(counter, get_happy(i)))
        counter = counter + 1

    with open(sys.argv[1] + 'output', 'w') as f:
        f.write('\n'.join(output))