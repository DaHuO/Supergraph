#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import copy

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

digits = [
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
]

def subarr(a, b):
    c = []
    for i in range(len(a)):
        if a[i] < b[i]:
            return None
        c.append(a[i]-b[i])
    return c

def to26arr(s):
    arr = [0]*26
    for c in s:
        arr[ord(c)-ord('A')] += 1
    return arr


def solve(s, digit26):
    s_arr = to26arr(s)
    answer = []

    for i in range(s_arr[25]):
        answer.append(0)
        s_arr = subarr(s_arr, digit26[0])

    for i in range(s_arr[23]):
        answer.append(6)
        s_arr = subarr(s_arr, digit26[6])

    for i in range(s_arr[6]):
        answer.append(8)
        s_arr = subarr(s_arr, digit26[8])

    for i in range(s_arr[18]):
        answer.append(7)
        s_arr = subarr(s_arr, digit26[7])

    for i in range(s_arr[22]):
        answer.append(2)
        s_arr = subarr(s_arr, digit26[2])

    for i in range(s_arr[21]):
        answer.append(5)
        s_arr = subarr(s_arr, digit26[5])

    for i in range(s_arr[5]):
        answer.append(4)
        s_arr = subarr(s_arr, digit26[4])

    for i in range(s_arr[14]):
        answer.append(1)
        s_arr = subarr(s_arr, digit26[1])

    for i in range(s_arr[17]):
        answer.append(3)
        s_arr = subarr(s_arr, digit26[3])

    while True:
        s_arr = subarr(s_arr, digit26[9])
        if s_arr != None:
            answer.append(9)
        else:
            break

    if s_arr and sum(s_arr) != 0:
        print 'kuso'
        print s_arr
    return ''.join(map(str, sorted(answer)))

if __name__ == '__main__':
    digit26 = []
    for d in digits:
        digit26.append(to26arr(d))

    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        answer = solve(f.readline().rstrip(), digit26)

        print "Case #%d: %s" % (i+1, answer)

# sort by key
# for k,v in sorted(d.items())
# sort by value
# for k,v in sorted(d.items(), key=lambda x:x[1])
# items() return tapple, tapple[0] is k, tapple[1] is v
#
# import copy
# copy.copy()
# copy.deepcopy()
#
# a = [0]*100
#
# for tc in xrange(1, int(sys.stdin.readline())+1):
#   A, B = [int(w) for w in sys.stdin.readline().split()]
#   p = [float(w) for w in sys.stdin.readline().split()]
#
# array = [[0 for j in range(m)] for i in range(n)]

