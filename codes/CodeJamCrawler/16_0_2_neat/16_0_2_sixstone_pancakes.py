#!/usr/bin/env python3

# Pancakes last element is - in this call, always
def r_flipping(pancakes):
    length = len(pancakes)
    if length == 0:
        return 0
    elif length == 1:
        return 1 if pancakes[0] == '-' else 0
    else:
        max_flip = 0
        initial = pancakes[0]
        for i in range(1, length):
            if pancakes[i] == initial:
                max_flip = i
            else:
                break

        # All -
        if initial == '+' and max_flip == length - 1:
            return 0

        # Flip!
        i = 0
        j = max_flip
        next_length = length
#        import pdb; pdb.set_trace()
        while i <= j:
            pancake = pancakes[i]
            pancakes[i] = '+' if pancakes[j] == '-' else '-'
            if i != j:
                pancakes[j] = '+' if pancake == '-' else '-'
            if j == next_length - 1  and pancakes[j] == '+':
                next_length -= 1
            i += 1
            j -= 1
        return r_flipping(pancakes[:next_length]) + 1


def flipping(pancakes):  
    max_flip = 0
    for i, c in enumerate(reversed(pancakes)):
        if c == '-':
            max_flip = len(pancakes) - i
            break

    return r_flipping(pancakes[:max_flip])


t = int(input())
for i in range(1, t+1):
    ps = list(input())
    r = flipping(ps)
    print("Case #{}: {}".format(i, r))
