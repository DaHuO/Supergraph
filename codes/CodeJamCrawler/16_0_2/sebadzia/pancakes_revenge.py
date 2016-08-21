def counter(function):
    def wrapper(*args):
        wrapper.called += 1
        return function(*args)
    wrapper.called = 0
    wrapper.__name__ = function.__name__
    return wrapper

@counter
def flip(stack, index):
    left, right = stack[:index+1], stack[index+1:]
    return invert(left[::-1]) + right

def invert(stack):
    return stack.replace('-', '%temp%').replace('+', '-').replace('%temp%', '+')

def any_unhappy(stack):
    return any([sign == '-' for sign in stack])

def find_last_unhappy(stack):
    return stack.rfind('-')

def find_first_unhappy(stack):
    return stack.find('-')

def solution(stack):
    flip.called = 0
    while any_unhappy(stack):
        first_unhappy = find_first_unhappy(stack)
        if first_unhappy > 0:
            stack = flip(stack, first_unhappy-1)
        stack = flip(stack, find_last_unhappy(stack))
    return flip.called

with open('input', 'r') as infile, open('output', 'w') as out:
    next(infile)
    for index, line in enumerate(infile):
        out.write("Case #{0}: {1}\n".format(index+1, solution(line)))
