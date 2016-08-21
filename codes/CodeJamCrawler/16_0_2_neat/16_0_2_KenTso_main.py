#!/usr/bin/env python

stack = ""


def flip(c):
    return "+" if c == "-" else "-"


def find(left, right, aim, is_reverse_complement):
    if left > right:
        return 0
    if left == right:
        return 0 if stack[left] == aim else 1

    if not is_reverse_complement:
        if stack[right] == aim:
            return find(left, right - 1, aim, is_reverse_complement)
        elif stack[left] != aim:
            return find(left, right, flip(aim), not is_reverse_complement) + 1
        else:
            for tmp in range(right - 1, left - 1, -1):
                if stack[tmp] == aim:
                    return find(left, tmp, flip(aim), is_reverse_complement) + 1
            else:
                return 1
    else:
        if stack[left] == aim:
            return find(left + 1, right, aim, is_reverse_complement)
        elif stack[right] != aim:
            return find(left, right, flip(aim), not is_reverse_complement) + 1
        else:
            for tmp in range(left + 1, right + 1):
                if stack[tmp] == aim:
                    return find(tmp, right, flip(aim), is_reverse_complement) + 1
            else:
                return 1


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    stack = raw_input()
    print "Case #{}: {}".format(i, find(0, len(stack) - 1, "+", False))
