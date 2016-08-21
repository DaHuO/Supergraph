#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "ludaoyuan1989@gmail.com (Daoyuan Lu)"
__copyright__ = "Copyright 2016 ludaoyuan1989@gmail.com (Daoyuan Lu). All Rights Reserved."


def main():
    fout = open("output", "w")
    with open("input", "r") as fin:
        T = int(fin.readline())
        Ss = [int(x) for x in fin.readlines()]
        for i in range(T):
            digit_set = set()
            if Ss[i] == 0:
                res = "INSOMNIA"
            else:
                cnt = 1
                while len(digit_set) != 10:
                    num = str(Ss[i] * cnt)
                    for digit in num:
                        digit_set.add(digit)
                    cnt += 1
                res = Ss[i] * (cnt - 1)
            print >> fout, "Case #%d: %s" % (i + 1, res)


if __name__ == '__main__':
    main()
