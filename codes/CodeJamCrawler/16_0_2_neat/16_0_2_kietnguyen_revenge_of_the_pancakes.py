#!/usr/bin/env python3

from collections import deque

def flip(stack):
    return ''.join(['+' if c == '-' else '-' for c in stack[::-1]])


def is_all_happy(stack):
    return list(stack).count('+') == len(stack)


def num_flips(stack):
    if is_all_happy(stack):
        return 0

    flip_queues = deque()
    flip_queues.append((0, stack))

    pancake_states = {stack}
    while len(flip_queues) > 0:
        #print(flip_queues)
        num_flip, stack = flip_queues.popleft()

        for i, _ in enumerate(stack, 1):
            new_stack = flip(stack[:i]) + stack[i:]

            if new_stack not in pancake_states:
                #print("Add", new_stack)
                if is_all_happy(new_stack):
                    return num_flip + 1

                pancake_states.add(new_stack)
                flip_queues.append((num_flip + 1, new_stack))



if __name__ == '__main__':
    t = int(input())
    for t in range(1, t + 1):
        pancakes = input()
        print('Case #%d: %s' % (t, num_flips(pancakes)))
