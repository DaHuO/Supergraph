#!/usr/bin/python

import sys

if __name__ == "__main__":    
    t = int(raw_input()) # read a line with single integer
    for i in range(1, t + 1):
        N = int(raw_input())
        dic = [0 for j in range(0,2501)]
        mh = 0
        for j in range(1, 2 * N - 1 + 1):
            list = [int(s) for s in raw_input().split(" ")]
            for k in range(0,N):
                dic[list[k]] += 1
                mh = max(mh,list[k])
        
        row = []
        for j in range(1,mh + 1):
            if dic[j] % 2 == 1:
                row.append(j)
        row.sort()
        print "Case #" + str(i) + ": ",
        for j in range(0,N):
            print str(row[j]) + " ",
        print ""
