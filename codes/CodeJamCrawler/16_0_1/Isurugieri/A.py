from Queue import * # Queue, LifoQueue, PriorityQueue
from bisect import * #bisect, insort
from collections import * #deque, Counter,OrderedDict,defaultdict
#set([]) 
import math
import copy
import itertools
import string
import sys
myread = lambda : map(int,raw_input().split())
def solver(x):
    if x == 0:
        return "INSOMNIA"
    N_,N = x,x
    memo = set()
    while True:
        for c in str(N):
            memo.add(c)
        if len(memo) == 10:
            return str(N)
        N += N_
    

if __name__ == "__main__":
    T = int(raw_input())
    for i in xrange(T):
        ans = solver(int(raw_input()))
        print "Case #%d: %s" % (i+1, ans)
    
