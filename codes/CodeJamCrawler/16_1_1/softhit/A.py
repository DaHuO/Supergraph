#!python3
import itertools
from  heapq import *

def solve(words):
    """y is the minimum number of moves to make the strings identical. If there is no possible way to make all strings identical, print "Fegla Won" (quotes for clarity)."""
    h = []
    for i,c in enumerate(words):
        idx = 0
        if i == 0:
            h.append(c)               # break
        else:
            if c >= h[0]:
                h.insert(0,c)
            else:
                h.append(c)

    w = "".join(h)
    return w


if __name__ == "__main__":
    import fileinput
    # f = fileinput.input()
    with open('sample.in') as f:
        """The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer N which is the number of strings. Followed by N lines, each line contains a non-empty string (each string will consist of lower case English characters only, from 'a' to 'z')."""

        T = int(f.readline())

        for case in range(1, T+1):
            words = f.readline().split()[0]
            answer = solve(words)
            print("Case #{0}: {1}".format(case, answer))