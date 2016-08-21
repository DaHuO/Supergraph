__author__ = 'pranavgupta'
from collections import defaultdict
import re


def start_count(N):
    if N == 0:
        return "INSOMNIA"
    else:
        i = 1
        unseen = [0,1,2,3,4,5,6,7,8,9]
        while(1):
            num = i * N
            num2 = num
            while(num>0):
                digit = num%10
                num = num/10
                try:
                    unseen.remove(digit)
                except:
                    pass
                if len(unseen) == 0:
                    return num2
            i += 1


if __name__ == '__main__':
    T = long(raw_input())
    for i in range(T):
        N = long(raw_input())
        answer = start_count(N)
        print "Case #{0}: {1}".format(i+1,answer)