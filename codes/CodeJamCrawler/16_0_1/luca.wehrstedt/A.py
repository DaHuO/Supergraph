#!/usr/bin/python3

def run():
    s = input().strip()
    res = s[0]
    for i in range(1, len(s)):
        if s[i] >= res[0]:
            res = s[i] + res
        else:
            res = res + s[i]
    return res

t = int(input().strip())
for i in range(t):
    print("Case #%d: %s" % (i+1, run()))
