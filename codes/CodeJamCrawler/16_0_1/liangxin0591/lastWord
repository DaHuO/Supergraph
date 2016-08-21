#!/usr/bin/python

import sys

def lastWord(s):
    res = []
    res.append(s[0])
    for i in range(1, len(s)):
        if [s[i]] + res[:] > res[:] + [s[i]]:
            res = [s[i]] + res[:]
        else:
            res = res[:] + [s[i]]
    res = "".join(res)
    return res


if __name__ == "__main__":
    
    t = int(raw_input()) # read a line with single integer
    for i in range(1, t + 1):
        S = raw_input()
        ss = lastWord(S)
        print("Case #" + str(i) + ": " + ss)
        
            
