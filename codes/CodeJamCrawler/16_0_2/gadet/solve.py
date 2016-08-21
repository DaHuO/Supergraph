import sys

def pancake_flip(stack, i):
    '''Flips the stack at the given index, 0 is top, n-1 is bottom'''
    top = list(stack[:i+1])
    top.reverse() # reverses the order of the flipped pancakes
    top = map(lambda p: '-' if p == '+' else '+', top) # flips the pancakes to the other side
    bottom = [stack[i+1:]]
    new_stack = ''.join(top + bottom)
    return new_stack

def min_flips(stack):
    '''Flips the stack at every index, until stack is all facing up ('+')
        + : side up pancake
        - : side down pancake
    Arguments:
        stack: pancake stack
    '''
    memoized_flips = {}
    stacks_to_check = [(stack, 0)]
    checked = set()
    while stacks_to_check:
        cur_stack, cur_flips = stacks_to_check.pop(0)
        if cur_stack not in checked:
            if cur_stack.count('+') == len(stack):
                return cur_flips
            else:
                for i in range(len(stack)):
                    new_stack = pancake_flip(cur_stack, i)
                    stacks_to_check.append((new_stack, cur_flips + 1))
            checked.add(cur_stack)

if __name__ == '__main__':
    data = sys.stdin.read()
    stacks = data.split('\n')[1:-1]
    for i, stack in enumerate(stacks, start=1):
        print "Case #{}: {}".format(i, min_flips(stack))
