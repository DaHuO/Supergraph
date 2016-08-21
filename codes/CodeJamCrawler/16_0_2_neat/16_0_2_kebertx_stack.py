#!/usr/bin/env python3

def flip_stack(stack, n):
    top, bottom = stack[:n], stack[n:]
    top = ''.join(reversed(top))
    top = top.translate(str.maketrans('+-', '-+'))
    # print(stack, '->', top + bottom)
    return top + bottom

def collapse_stack(stack):
    if stack == '':
        return ''

    symbols = [stack[0]]
    for i, c in enumerate(stack[1:]):
        if c != stack[i]:
            symbols.append(c)
    return ''.join(symbols)

def count_flips(stack):
    stack = collapse_stack(stack).rstrip('+')

    if stack == '':
        return 0
    elif stack.find('+') == -1:
        return 1
    else:
        count = 0
        if stack[0] == '+':
            count += 1
            stack = flip_stack(stack, 1)
        stack = flip_stack(stack, len(stack))
        count += 1 + count_flips(stack)

        return count

with open('B-large.in', 'r') as infile:
    lines = infile.readlines()[1:]
    for i, n in enumerate(lines):
        print("Case #{}:".format(i + 1), count_flips(n.strip()))
