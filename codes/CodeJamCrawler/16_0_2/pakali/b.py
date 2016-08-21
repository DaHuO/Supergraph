import sys
import string

def find_pancake(stack):
    pancake = len(stack)
    last = None

    for i in xrange(pancake):
        if last == None:
            last = stack[i]
            continue

        if stack[i] != last:
            return i - 1

    return pancake - 1

def flip(stack, index):
    my_stack = stack[:(index + 1)]
    my_stack = my_stack.translate(string.maketrans("+-", "-+"))
    my_stack = my_stack + stack[(index + 1):]
    return my_stack

def revenge_of_the_pancakes(stack, test_case):
    t = 0
    while True:
        if "-" not in stack:
            break
        
        stack = flip(stack, find_pancake(stack))
        t += 1

    print "Case #%d: %d" % (test_case, t)

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        s = f.readline().split()

        revenge_of_the_pancakes(str(s[0]), _t+1)