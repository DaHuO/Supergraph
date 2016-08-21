__author__ = 'pranavgupta'
from collections import defaultdict
import re


def insertChar(mystring, position, chartoinsert ):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:]
    return mystring


def largest_S(S):
    answer = S[0]
    # insert in answer string at correct posn in increasing order
    for c in S[1:]:
        i = 0
        if c >= answer[0]:
            answer = c + answer
        else:
            answer += c
    return answer


if __name__ == '__main__':
    T = long(raw_input())
    for i in range(T):
        S = raw_input()
        answer = largest_S(S)
        print "Case #{0}: {1}".format(i+1,answer)