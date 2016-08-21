#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "ludaoyuan1989@gmail.com (Daoyuan Lu)"
__copyright__ = "Copyright 2016 ludaoyuan1989@gmail.com (Daoyuan Lu). All Rights Reserved."

def main():
    fout = open("output", "w")
    with open("input", "r") as fin:
        T = int(fin.readline())
        Ss = [x[:-1] for x in fin.readlines()]
        for i in range(T):
            cnt = 0
            for j in range(1, len(Ss[i])):
                if Ss[i][j] != Ss[i][j-1]:
                    cnt += 1
            res = cnt if Ss[i][0] == '+' and cnt % 2 == 0 or Ss[i][0] == '-' and cnt % 2 == 1 else cnt + 1
            print >> fout, "Case #%d: %d" % (i + 1, res)



if __name__ == '__main__':
    main()
