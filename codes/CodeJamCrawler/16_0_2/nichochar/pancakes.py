#!usr/local/bin/python
import sys
data = sys.stdin.readlines()

number_of_cases = int(data[0])


def solve_one(stack):
    """Returns the min number of times you have to
    flip the stack to get it all up

    Basically start at the end, decrement, increment a counter
    when the side changes (current_side starts at +) and
    increment one last time if you hit 0 and the counter is -
    """
    current_dir = '+'
    counter = 0
    for i in xrange(len(stack) - 1, 0, -1):
        if current_dir != stack[i - 1]:
            counter += 1
            current_dir = stack[i - 1]

    return counter


for i in xrange(number_of_cases):
    max_hit = solve_one(data[i + 1])
    print "Case #%s: %s" % (i + 1, max_hit)
