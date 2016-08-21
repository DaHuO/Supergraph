#!/usr/bin/env python3

def parse():
    s = input()
    return s

def solve(s):
    k = s[0]
    for c in s[1:]:
        if c < k[0]: k = k + c
        else: k = c + k
    return k

def main():
    for i in range(int(input())):
        s = parse()
        k = solve(s)
        print("Case #{}: {}".format(i+1, k))

if __name__ == "__main__": main()
