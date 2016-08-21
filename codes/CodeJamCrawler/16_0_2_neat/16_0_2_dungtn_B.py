import sys


def is_all_up(state):
    return '-' not in set(state)


def flip(state):
    res = []
    for side in state:
        if side == "+":
            res.append("-")
        else:
            res.append("+")
    return "".join(res[::-1])


def get_children(state):
    for i in xrange(1, len(state)+1):
        yield flip(state[:i]) + state[i:]


def bfs(start):
    visited, queue = set(), [(start, [])]

    while queue:
        vertex, path = queue.pop(0)
        if is_all_up(vertex):
            return path + [vertex]
        if vertex not in visited:
            visited.add(vertex)
            for child in get_children(vertex):
                queue.append((child, path + [vertex]))
    return None


def main():
    f = open(sys.argv[1], 'r')
    T = int(f.readline().strip())

    for t in xrange(T):
        stack = f.readline().strip()
        print "Case #{0}: {1}".format(t+1, len(bfs(stack))-1)


if __name__=="__main__":
    main()