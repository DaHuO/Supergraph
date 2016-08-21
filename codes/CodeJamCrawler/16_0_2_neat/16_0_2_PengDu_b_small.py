#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    for case_id in xrange(1, N + 1):
        pancakes = sys.stdin.readline()[:-1]
        target = '+' * len(pancakes)
        states = {
            pancakes: 0
        }
        queues = [pancakes]
        while len(queues) > 0:
            top = queues.pop(0)
            steps = states[top]
            if top == target:
                break
            for flip_end in xrange(1, len(top) + 1):
                new_pancakes = ''.join(['+' if ch == '-' else '-' for ch in top[:flip_end][::-1]]) + top[flip_end:]
                if new_pancakes not in states:
                    states[new_pancakes] = steps + 1
                    queues.append(new_pancakes)
        print "Case #%d: %d" % (case_id, states[target])
