#!/usr/bin/env python

def flip_to(i, a):
    return [not e for e in reversed(a[:i])] + a[i:]

def numflips(arr):
    end = [True]*len(arr)
    n = 0
    for i, e in reversed(list(enumerate(arr))):
        if e != end[i]:
            end = flip_to(i+1, end)
            n += 1
    # print arr, n, end
    # assert(arr == end)
    return n


def readstack(stackstr):
    return [p == '+' for p in stackstr]

def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s: %s' % (i+1, numflips(readstack(raw_input())))

if __name__ == "__main__":
    main()
