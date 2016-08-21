def min_flips(stack):
    if len(stack) == 0:
        return 0

    elif stack[0] == '-':
        try:
            pivot = stack.index('+')
            return 2 + min_flips(stack[pivot:])
        except ValueError:
            return 1

    elif stack[0] == '+':
        try:
            pivot = stack.index('-')
            return 0 + min_flips(stack[pivot:])
        except ValueError:
            return 0


def solve(stack):
    stack.reverse()
    return min_flips(stack)


if __name__ == '__main__':
    with open('input.txt') as f:
        cases = int(f.readline())
        for i in xrange(cases):
            print "Case #{i}: {solution}".format(
                i=i + 1, solution=solve(list(f.readline().strip())))
