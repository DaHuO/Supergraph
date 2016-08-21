#!/usr/bin/env python3

def main(*args):
    s = args[0]
    lw = ''
    for c in s:
        if all(c >= d for d in lw):
            lw = c + lw
        else:
            lw = lw + c
    return lw

if __name__ == '__main__':
    for i in range(int(input())):
        print("Case #{}: {}".format(i + 1, main(*input().split())))
