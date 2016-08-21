"""
Google Code Jam 2016
Problem A. Counting Sheep
Author: Amit Kumar | dtu.amit@gmail.com
"""


def solve(n):
    s, i = set(), 1
    if n == 0:
        return "INSOMNIA"
    while len(s) != 10:
        n_new = n*i
        ans = n_new
        while n_new:
            s.add(n_new % 10)
            n_new = n_new/10
        i += 1
    return ans

T = int(input())

for i in range(1, T + 1):
    n = int(input())
    print ("Case #%s: %s" % (i, solve(n)))
