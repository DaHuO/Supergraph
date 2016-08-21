# 2016-QR-B: Pancake REVENGE

DEBUG = False

def flip(stack, depth):
    if depth < 1 or depth > len(stack):
        print "%s: %s -> !!" % (depth, to_str(stack))
        raise Exception("invalid flip")
    flipped = [not i for i in stack[0:depth]]
    flipped.extend(stack[depth:])
    if DEBUG:
        print "%s: %s -> %s" % (depth, to_str(stack), to_str(flipped))
    return flipped

def parse(str_in):
    """Parse the input string into a stack"""
    return [c == '+' for c in list(str_in)]

def to_str(stack):
    """Return a string for the given stack"""
    return ''.join(['+' if p else '-' for p in stack])

def leading_pos(stack):
    """Return count of leading positive pancakes"""
    for i, val in enumerate(stack):
        if val == False:
            return i
    # the whole stack is happy side up
    return len(stack)

def last_neg(stack):
    """Return position of last negative pancake"""
    for i, val in reversed(list(enumerate(stack))):
        if val == False:
            # +1 because we want the flip to include this pancake
            return i + 1
    # all happy side up already
    return 0

def solve(stack, moves=0):
    """Solve the flipping problem. Return min number of moves."""
    # Algorithm:
    # We want first pancake to be -, so it ends as + after we flip it.
    # Flipping it will also push it to the bottom of the stack.
    # Any + on the bottom of the stack are fixed.
    pos = leading_pos(stack)
    if pos == len(stack):
        # solved
        return moves
    elif pos > 0:
        # First pancake is up
        stack = flip(stack, pos)
        return solve(stack, moves + 1)
    else:
        # First pancake is down.
        # When we flip, it will increase trailing_pos
        # The flip point should be the last down-facing pancake
        neg = last_neg(stack)
        stack = flip(stack, neg)
        return solve(stack, moves + 1)

def main():
    num_cases = int(raw_input())
    for case_id in xrange(num_cases):
        stack = parse(raw_input())
        moves = solve(stack)
        print "Case #{0}: {1}".format(case_id + 1, moves)

if __name__ == "__main__":
    main()
