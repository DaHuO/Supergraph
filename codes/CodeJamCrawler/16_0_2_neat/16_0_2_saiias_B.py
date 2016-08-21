#! /usr/bin/env python
# -*- coding: utf-8 -*-


def solve(inp):

    ans = 0

    point = len(inp)
    while True:
        if inp.count('+') == len(inp):
            return ans

        if inp[point-1] == '+':
            point = point - 1
        else:
            ans = ans + 1
            temp = []
            for i in xrange(point):
                if inp[i] == '+':
                    temp.append('-')
                else:
                    temp.append('+')
            inp = ''.join(temp) + inp[point:]

 
def main():
    N = int(raw_input())

    for i in xrange(N):
        ans = solve(raw_input())
        print "Case #{}: {}".format(i+1, ans)
    return 0

if __name__ == "__main__":
    main()
