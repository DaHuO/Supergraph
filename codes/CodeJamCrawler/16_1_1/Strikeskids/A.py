#!/usr/bin/env python3

from collections import deque

def compute_last(word):
    arr = deque()

    high = 'A'
    for c in word:
        if c >= high:
            arr.appendleft(c)
            high = c
        else:
            arr.append(c)

    return ''.join(arr)

def run_test(i):
    word = input()
    print('Case #%d: %s' % (i, compute_last(word)))

def main():
    T = int(input())

    for t in range(T):
        run_test(t+1)

def extensive():
    import random
    for i in range(100000):
        compute_insomnia(random.randint(0, 10**6))
    exit(0)

if __name__ == '__main__': main()