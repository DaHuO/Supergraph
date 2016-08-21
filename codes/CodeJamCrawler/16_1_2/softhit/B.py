#!python3
import itertools
from  heapq import *

def solve(N,L):
    """y is the minimum number of moves to make the strings identical. If there is no possible way to make all strings identical, print "Fegla Won" (quotes for clarity)."""
    L = sorted(L)
    R = []
    # FIll table:
    # Find min, find max
    b = [0] * 2500
    for j in range(0, 2 * N - 1):
        for k in range(0, N):
            tmp = L[j][k] - 1
            b[tmp] += 1

    for j in range(0, 2500):
        if b[j] % 2 != 0:
            R.append(j + 1)
        # find maxi, check if maxi appears twice
    ans = " ".join(map(str,R))
    return ans


if __name__ == "__main__":
    import fileinput
    # f = fileinput.input()
    with open('sample.in') as f:
        """The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer N which is the number of strings. Followed by N lines, each line contains a non-empty string (each string will consist of lower case English characters only, from 'a' to 'z')."""

        T = int(f.readline())

        for case in range(1, T+1):
            N = int(f.readline())
            L = []
            for i in range(2*N -1):
                L.append( list(map(int,f.readline().split())))
            answer = solve(N,L)
            print("Case #{0}: {1}".format(case, answer))