def inverse(stack):
    """
    Inverse the stack
    """
    return [not elem for elem in stack]


def flip(stack, n):
    """
    Flip and inverse the first n elements of the stack
    """
    return inverse(stack[:n][::-1]) + stack[n:]


def first_different(stack):
    i = 0
    first_elem = None

    for i, elem in enumerate(stack):
        if first_elem is None:
            first_elem = elem
        if elem != first_elem:
            break
    else:
        return i + 1

    return i


def compute(N):
    i = 0

    while not all(N):
        N = flip(N, first_different(N))
        i += 1
    return i


def parse(N):
    return [x == '+' for x in N]


def main():
    T = input()
    for N in xrange(T):
        print "Case #{}: {}".format(N + 1, compute(parse(raw_input())))

if __name__ == "__main__":
    main()
