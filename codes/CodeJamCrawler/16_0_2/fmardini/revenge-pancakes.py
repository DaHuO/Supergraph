import os, sys

f = lambda p: '+' if p == '-' else '-'
def flip(pancakes, idx):
    k = idx - 1
    for i in range(idx / 2):
        t = pancakes[k]
        pancakes[k] = f(pancakes[i])
        pancakes[i] = f(t)
        k -= 1
    if idx % 2 == 1:
        pancakes[idx / 2] = f(pancakes[idx / 2])
    return pancakes

def eat(ps, c, i):
    l = len(ps)
    while i < l and pancakes[i] == c:
        i += 1
    return i

def solve(pancakes):
    k, i = 0, 0
    l = len(pancakes)
    while True:
        while i < l and pancakes[i] == '-':
            i += 1
        if i == l:
            return k + 1
        if i > 0:
            flip(pancakes, i)
            k += 1
            i = 0
            next
        while i < l and pancakes[i] == '+':
            i += 1
        if i == l:
            return k
        while i < l and pancakes[i] == '-':
            i += 1
        if i == l:
            return k + 2
        for j in range(i):
            pancakes[j] = '+'
        k += 2
        i = 0

T = int(sys.stdin.readline().strip())
for k in range(T):
    pancakes = [c for c in sys.stdin.readline().strip()]
    print("Case #{}: {}".format(k + 1, solve(pancakes)))
