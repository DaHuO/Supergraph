#!/usr/bin/env python3

from queue import PriorityQueue


def heuristic(s):
    return 0 #len([c for c in s if c == "-"])


def successors(s):
    for i in range(1, len(s) + 1):
        first_part = s[:i]
        second_part = s[i:]

        succ = "".join(("+" if c == "-" else "-") for c in first_part[::-1]) + second_part
        yield succ


def pancake_flips(s):
    # A* search searching through the possible flips.
    open_nodes = PriorityQueue()
    initial_h = heuristic(s)
    open_nodes.put((initial_h, initial_h, 0, s))

    closed = set()
    distance = {}

    while not open_nodes.empty():
        f, h, g, node = open_nodes.get()
        if node not in closed or g < distance[node]:
            closed.add(node)
            distance[node] = g

            if all(c == "+" for c in node):
                return g
            for succ in successors(node):
                hs = heuristic(succ)
                gs = g + 1
                fs = hs + gs
                open_nodes.put((fs, hs, gs, succ))
    raise Exception("Not possible to get here.")


def main():
    t = int(input())
    for i in range(1, t + 1):
        s = input()
        y = pancake_flips(s)
        print("Case #{}: {}".format(i, y))


if __name__ == "__main__":
    main()
