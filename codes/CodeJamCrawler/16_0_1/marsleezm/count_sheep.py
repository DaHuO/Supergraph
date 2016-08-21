#!/usr/bin/env python3

import sys


def getresult(num):
    count = 10
    array = [0]*10
    counted = {}
    nownum = 0 
    tmpnum = 0
    while True:
        nownum += num
        if nownum in counted:
            return "INSOMNIA" 
        counted[nownum] = 1
        tmpnum = nownum
        while tmpnum > 0:
            rem = tmpnum % 10
            if array[rem] == 0:
                count -= 1 
                array[rem] += 1
            if count == 0:
                return str(nownum)
            tmpnum = int(tmpnum / 10)

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for ind in range(1,t+1):
        num = int(f.readline())
        result = getresult(num)
        print("Case #"+str(ind)+": "+result)
