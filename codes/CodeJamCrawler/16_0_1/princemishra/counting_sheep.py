import sys
import os
import time

def solve(n):
    #print "solving ", n
    if n==0:
        return "INSOMNIA"
    found = set()
    __start = time.time()
    i = 1
    while True:
        if len(found) == 10:
            break
        cur = n*i
        digits = str(cur)
        for d in digits:
            found.add(d)
            if len(found) == 10:
                #print "######breaking when found", cur, found
                break

        # if time.time() - __start > 5:#2*60:
        #     print "too long ", n, i, cur
        #     break
        i += 1
    return cur


if __name__=="__main__":
    T = input()
    for i in range(T):
        n = input()
        print "Case #%s: %s" % (i+1, solve(n))
    #n = raw_input()
    # for i in range(0,100000):
    #     print i, solve(i)
    



