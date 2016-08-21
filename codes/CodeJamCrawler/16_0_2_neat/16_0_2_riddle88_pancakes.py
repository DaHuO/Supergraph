__author__ = 'pranavgupta'
from collections import defaultdict
import re


def count_tosses(S):
    count = 0
    last_elem = "+"
    for i in range(len(S)-1,-1,-1):
        elem = S[i]
        # print i
        # print elem
        if elem!=last_elem:
            count += 1
        last_elem = elem
    return count


if __name__ == '__main__':
    T = long(raw_input())
    for i in range(T):
        S = raw_input()
        answer = count_tosses(S)
        print "Case #{0}: {1}".format(i+1,answer)