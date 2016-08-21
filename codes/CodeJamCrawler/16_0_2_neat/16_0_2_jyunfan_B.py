import sys
import numpy as np

T = sys.stdin.readline()

def flip_pancake(pancakes):
    pancakes = [True if p=='+' else False for p in pancakes]
#    print(pancakes)
    n = len(pancakes)
    final_state = [True] * n
    count = 0
    while final_state != pancakes:
        count += 1
        top = pancakes[0]
        for i in range(0,n):
            if pancakes[i] != top:
                break
            pancakes[i] = not pancakes[i]
#        print(pancakes)

    return count


case = 1
for line in sys.stdin:
    pancakes = list(line.strip())
    print('Case #%d: %d' % (case, flip_pancake(pancakes)))
    case += 1
