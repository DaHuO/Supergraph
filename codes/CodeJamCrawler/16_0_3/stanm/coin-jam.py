#! /usr/bin/python

import sys

def rinp():
    one = input()
    _ = input().split(' ')
    N = int(_[0])
    J = int(_[1])
    return (N, J)

def get_binary(num):
    return "{0:b}".format(num)

def in_base(stng, base):
    return int(stng, base)

def get_div(x):
    for d in range(2, x):
        if d * d > x:
            return 1
        if x % d == 0:
            return d

def check_num(x):
    bnry = get_binary(x)
    divs = []
    for base in range(2, 11):
        t = in_base(bnry, base)
        div = get_div(t)
        if div == 1:
            return 0
        divs.append(div)

    print (bnry, " ".join([str(d) for d in divs]))
    return 1

def main():
    (N, J) = rinp()
    start = 2 ** (N - 1) + 1
    end = 2 ** N - 1
    print ("Case #1:")
    count = 0
    for x in range(end, start, -2):
        get_binary(x)
        count += check_num(x)
        if count == J:
            break


if __name__ == '__main__':
    main()
