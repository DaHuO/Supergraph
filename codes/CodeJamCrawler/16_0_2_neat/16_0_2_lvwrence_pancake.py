import sys

HAPPY = '+'
SAD = '-'

def pancake(stack):
    n = 0
    while SAD in stack:
        i = stack.rfind(SAD) + 1
        stack = flip(stack, i)
        n += 1
    return n

def flip(stack, i):
    flipped_part = ''.join([HAPPY if x == SAD else SAD for x in stack[:i]])
    rest = stack[i:]
    return flipped_part + rest


if __name__ == "__main__":
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        stack = raw_input()  # read a pancake stack
        print "Case #{}: {}".format(i, pancake(stack))
