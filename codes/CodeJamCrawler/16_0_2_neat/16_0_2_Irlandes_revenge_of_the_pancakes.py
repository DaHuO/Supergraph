__author__ = 'fdoherty'


def output(case, data):
    print 'Case #%s:' % case, data

def reverse_bits(stack):
    stack = stack.replace('-', '.')
    stack = stack.replace('+', '-')
    stack = stack.replace('.', '+')
    return stack

def flip_stack(stack):
    x = reverse_bits(stack)
    return x[::-1]

def perform_flip(stack, quantity):
    flipped = flip_stack(stack[0:quantity])
    new_stack = '%s%s' % (flipped, stack[quantity:])
    #print '.. %s %s >> %s' % (stack, quantity, new_stack)
    return new_stack

def consecutive_from_right(stack, char):
    return len(stack) - stack.rfind(char) - 1

def consecutive_from_left(stack, char):
    return stack.find(char)

def solve(case_num, stack):
    all_digits = set()
    iterations = 0
    x = len(stack)
    while iterations < 10000 and x > -1:
        if stack.find('-') < 0:
            output(case_num, iterations)
            return
        if stack[x-1] == '-':
            max_to_flip = consecutive_from_left(stack[:x], '-')
            if max_to_flip > 0:
                stack = perform_flip(stack, max_to_flip)
                iterations += 1
            stack = perform_flip(stack, x)
            iterations += 1
        x -= 1
    output(case_num, iterations)


NUM_CASES = input()
for test_num in range(NUM_CASES):
    stack = raw_input()
    solve(test_num+1, stack)