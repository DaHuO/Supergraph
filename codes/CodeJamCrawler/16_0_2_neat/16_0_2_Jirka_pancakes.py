from itertools import dropwhile, takewhile

def opt(pancakes):
    if all(map(lambda x: x == '+', pancakes)):
        return 0
    head = list(reversed(list(dropwhile(lambda x: x == '+', reversed(pancakes)))))
    first = head[0]
    to_flip = len(list(takewhile(lambda x: x == first, head)))
    flipped = flip(to_flip, head)
    return opt(flipped) + 1

def flip(i, pancakes):
    group = pancakes[:i]
    fliped = map(lambda x: '-' if x == '+' else '+', group)
    return ''.join(list(list(reversed(list(fliped))) + list(pancakes[i:])))




# MAIN
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()[1:]):
        print('Case #' + str(i+1) + ': ' + str(opt(line[:-1])))

