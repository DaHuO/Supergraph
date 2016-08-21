#!/usr/bin/python3

def flip(s,n):
    s = [c for c in s]
    for i in range(n):
        if s[i] == "+":
            s[i] = "-"
        elif s[i] == "-":
            s[i] = "+"
        else:
            assert False
    return "".join(s)

def find_contiguous(s):
    if s[0] == "+":
        i = 0
        while s[i] == "+":
            i+=1
            if i == len(s):
                break
        return i
    elif s[0] == "-":
        i = 0
        while s[i] == "-":
            i+=1
            if i == len(s):
                break
        return i

def solve(s):
    num_flips = 0
    while "-" in s:
        i = find_contiguous(s)
        s = flip(s,i)
        num_flips += 1
    return num_flips

t = int(input())
for i in range(1,t+1):
    s = input()
    print("Case #%d: %d" % (i, solve(s)))
