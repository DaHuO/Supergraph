# Code Jam 2016
# Raoul Veroy
import fileinput

stdin = fileinput.input()

# Constants
# MAXLEN = 10 # for small
MAXLEN = 100 # for BIG
# Global results
results = {}
# Generate easy known results
# If they're all smiley face up, minimum flips is 0.
# If they're all smiley face down, minimum flips is 1.
for i in xrange(1, MAXLEN):
    s = "+" * i
    results[s] = 0
    s = "-" * i
    results[s] = 1

def flip_stack( stack ):
    result = ""
    for x in stack:
        if x == "+":
            result += "-"
        elif x == "-":
            result += "+"
        else:
            assert(False)
    assert(len(result) == len(stack))
    return result

def get_min_flips( stack = "" ):
    global results
    assert(len(stack) > 0)
    if stack in results:
        return results[stack]
    else:
        # Start from bottom and look for first "-"
        pos = stack.rfind("-")
        # Then find the largest string of "-" from there moving left
        left = pos
        while (left - 1) > 0 and stack[left - 1] == "-":
            left -= 1
        if left == 0:
            results[stack] = 1
            return results[stack]
        else:
            flips = 1 + get_min_flips( flip_stack(stack[0:left]) )
            results[stack] = flips
            return results[stack]

count = int(stdin.next())
for x in xrange(count):
    stack = stdin.next().rstrip()
    flips = get_min_flips(stack)
    print "Case #%d: %d" % (x+1, flips)
