#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(N):
    # print("[debug] solving %s" % (N))

    count_by_number = dict()
    result = []
    for i in xrange(0, 2 * N - 1):
        for j in raw_input().split():
            j = int(j)
            if (j not in count_by_number):
                count_by_number[j] = 0;
            count_by_number[j] = count_by_number[j] + 1

    # print("[debug] count_by_number %s" %(count_by_number))

    for k, v in count_by_number.iteritems():
        # print("[debug] k: %s, v: %s" % (k, v))
        if (v % 2 != 0):
            result.append(k)

    return " ".join([str(a) for a in sorted(result)])

    # return " ".join([str(a) for a in sorted(result, cmp=lambda x,y: x<y)]);

if __name__ == "__main__":
    testcases = input()

    for i in xrange(1, testcases+1):
        N = int(raw_input())
        print("Case #%i: %s" % (i, solve(N)))