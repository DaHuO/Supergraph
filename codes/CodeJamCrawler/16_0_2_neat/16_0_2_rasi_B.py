import sys
import itertools

def flip(pancakes, num):
    return [not x for x in pancakes[:num][::-1]] + pancakes[num:]

def remove_tail(pancakes):
    tail_len = len(list(itertools.takewhile(lambda x: x, pancakes[::-1])))
    return pancakes[:len(pancakes) - tail_len]

def calculate(pancakes):
    i = 0
    while True:
        pancakes = remove_tail(pancakes)
        l = len(pancakes)
        if l == 0:
            return i
        trues = len(list(itertools.takewhile(lambda x: x, pancakes)))
        i += 1
        if trues == 0:
            falses = len(list(itertools.takewhile(lambda x: not x, pancakes)))
            if falses == l:
                return i
            else:
                pancakes = flip(pancakes, falses)
        else:
            pancakes = flip(pancakes, trues)

for i in range(1, int(sys.stdin.readline()) + 1):
    pancakes = [c == '+' for c in sys.stdin.readline().strip()]
    res = calculate(pancakes)
    print('Case #%d: %d' % (i, res))
