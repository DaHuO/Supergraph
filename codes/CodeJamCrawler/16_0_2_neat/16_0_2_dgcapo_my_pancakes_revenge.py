#!/usr/bin/python
# -*- coding: utf-8 -*-

PLUS = '+'
MINUS = '-'

def simple_flip(pancake):
    assert pancake in [PLUS, MINUS]

    if pancake == PLUS:
        return MINUS
    else:
        return PLUS

def flip(pancake_group, acc_min_times):
    result = []
    # returns the flipped list and update the minimum times
    if pancake_group in ["", "+"]:
        acc = acc_min_times.pop()
        acc_min_times.add(acc)
        result = pancake_group
    elif pancake_group == "-":
        acc = acc_min_times.pop() + 1
        acc_min_times.add(acc)
        result = "+"
    else:
        # indices with a minus
        minus_list = [id for id, e in enumerate(pancake_group) if e == MINUS]
        if not minus_list:
            result = pancake_group
        else:
            selected_id = minus_list[-1]
            group = pancake_group[:selected_id + 1]

            intermediate_stack = []
            while(len(group) > 0):
                fst, group = group[0], group[1:]
                intermediate_stack.append(simple_flip(fst))

            pancake_group = "".join(intermediate_stack + list(pancake_group[selected_id + 1:]))
            acc = acc_min_times.pop() + 1
            acc_min_times.add(acc)
            result = flip(pancake_group, acc_min_times)

    return result

t = int(raw_input())
for i in xrange(1, t + 1):
    in_str = raw_input()


    result = set([0])
    flip(in_str, result)
    print "Case #{}: {}".format(i, result.pop())
