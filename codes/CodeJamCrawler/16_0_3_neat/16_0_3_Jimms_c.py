#!/usr/bin/python3

import sys
import math
import collections

def all(k):
    if k == 1:
        return ['0', '1']
    else:
        ret = []
        lowers = all(k - 1)
        for item in lowers:
            ret.append('0' + item)
            ret.append('1' + item)

        return ret

dic = {0: None}
def ret_fac(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i

    # is prime
    return None

def test(s):
    output = []
    for i in range(2, 11):
        n = int(s, i)
        # print("test" + s + "[" + str(n) + "] with base " + str(i))
        if n in dic:
            ret = dic[n]
        else:
            ret = ret_fac(n)
            dic[n] = ret
        if ret is None:
            return False
        output.append(str(ret))

    return output


def f(line):
    n, j = line.split(" ")
    n = int(n)
    j = int(j)

    done = 0
    for item in all(n):
        if item[0] != '1' or item[-1] != '1':
            continue
        ret = test(item)
        if ret:
            print(" ".join([item] + ret))
            done += 1
            if done == j:
                break


def main():
    n = int(input())
    for i in range(1, int(n) + 1):
        line = input()
        line = line.strip()
        print("Case #" + str(i) + ":")
        ans = f(line)
        n = n + 1


if __name__ == "__main__":
    main()
