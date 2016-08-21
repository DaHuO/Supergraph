from __future__ import print_function
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def solve(m):
    remainSet = set([0,1,2,3,4,5,6,7,8,9])
    historySet = set()
    count = 1
    n = m
    while True:
        r = n
        nonZero = n

        while True:
            x = r % 10
            remainSet.discard(x)

            if len(remainSet) == 0:
                return n
            
            if x != 0 and nonZero == -1 :
                nonZero = r
            if r < 10 :
                break
            
            r = r // 10
            
        if nonZero in historySet :
            return "INSOMNIA"
        else :
            historySet.add(nonZero)
        n += m    
        count += 1
        
    return -1

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        print("Case #%d: " % (i + 1)  , end="")
        print(solve(n))
    

def log(*message):
    logging.debug(*message)
    
if __name__ == "__main__":
    main()
