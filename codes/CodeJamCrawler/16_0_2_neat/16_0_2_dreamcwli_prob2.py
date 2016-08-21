#!/usr/bin/env python

cases = raw_input()
cases = int(cases)

for case in range(1, cases + 1):
    pancakes = raw_input()
    pancakes = list(pancakes)

    length = len(pancakes)
    count = 0
    for bottom in range(length - 1, -1, -1):
        if pancakes[bottom] == '-':
            flip = -1
            for top in range(bottom):
                if pancakes[top] == '-':
                    break
                else:
                    flip = top
            count += 1 if flip > -1 else 0
            for position in range(flip + 1, bottom + 1):
                pancakes[position] = '+' if pancakes[position] == '-' else '-'
            pancakes[:bottom + 1] = pancakes[bottom::-1]
            count += 1

    output = 'Case #%d: %d' % (case, count)
    print(output)
