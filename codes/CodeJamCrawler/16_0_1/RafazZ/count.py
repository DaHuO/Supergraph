#!/usr/bin/env python

def count(num):
    # if not num.isnumeric():
    #    return "INSOMNIA"
    if num == 0:
        return "INSOMNIA"
    base = {0,1,2,3,4,5,6,7,8,9}
    seen = set()

    counter = 1
    num1 = str(num)
    while True:
        # Add to seen:
        # print seen, num
        for c in num1:
            seen.add(int(c))
        if base == seen:
            return num1
        else:
            # num *= counter
            num1 = str(num * counter)
            counter += 1
    
    
for idx in range(1, input()+1):
    print "Case #%d:"%idx, count(input())
    
