from Queue import Queue


def minimal_flips(stack):
    queue = Queue()
    queue.put((0, stack))
    visited = set()
    all_smiley = all

    while not queue.empty():
        n_flips, stack = queue.get()
        visited.add(stack)

        if all_smiley(stack):
            return n_flips

        for s in successors(stack):
            if not s in visited:
                queue.put((n_flips + 1, s))


def successors(stack):
    for i in xrange(1, len(stack) + 1):
        yield flip(i, stack)


def flip(i, stack):
    top, bottom = stack[:i], stack[i:]
    new_top = tuple(1 if pancake is 0 else 0 for pancake in reversed(top))
    return new_top + bottom


def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        S = raw_input()
        stack = tuple(1 if char is '+' else 0 for char in S)
        print 'Case #{}: {}'.format(t, minimal_flips(stack))


if __name__ == '__main__':
    main()
