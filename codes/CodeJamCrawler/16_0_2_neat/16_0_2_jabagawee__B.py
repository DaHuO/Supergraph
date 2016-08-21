#! /usr/bin/env python

import itertools
import string
import Queue
transtable = string.maketrans('+-', '-+')


class Stack(object):
    def __init__(self, pancakes):
        pancakes = pancakes.rstrip('+')
        pancakes = ''.join(k for k, v in itertools.groupby(pancakes))
        self.pancakes = pancakes

    def num_flips(self):
        fringe = Queue.PriorityQueue()
        closed = set()
        fringe.put((0, self))
        while fringe:
            length, node = fringe.get()
            if node.done():
                return length
            if node not in closed:
                closed.add(node)
                for child in node.children():
                    fringe.put((length + 1, child))

    def children(self):
        for i in reversed(range(1, len(self.pancakes) + 1)):
            yield self.flip(i)

    def flip(self, n):
        pancakes = self.pancakes
        top, bottom = pancakes[:n], pancakes[n:]
        return Stack(top[::-1].translate(transtable) + bottom)

    def done(self):
        return set(self.pancakes) == set('+') or len(self.pancakes) == 0

    def __repr__(self):
        return self.pancakes

    def __hash__(self):
        return hash(self.pancakes)

    def __len__(self):
        return len(self.pancakes)

    def __eq__(self, other):
        return self.pancakes == other.pancakes

T = int(raw_input())
for i in range(T):
    S = Stack(raw_input())
    print 'Case #{}: {}'.format(i + 1, S.num_flips())
