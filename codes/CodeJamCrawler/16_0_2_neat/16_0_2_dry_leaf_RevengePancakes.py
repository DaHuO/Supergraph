#!/usr/bin/python
# -*- coding: utf-8 -*-

def RevengePancakes():
    file = open("B-large.in")
    T = int(file.readline())

    out = open("B-large.out", "w")
    for n in range(T):
        pank = file.readline().strip()
        S = [ch for ch in pank]

        happyside = S.count('+')
        times = 0

        while happyside != len(S):

            if S[0] == '+':
                for i in range(len(S)):
                    # print "Pos S = ", S[i]
                    if S[i] != '+':
                        break
                    else:
                        S[i] = '-'
            else:
                for i in range(len(S)):
                    # print "Neg S = ", S[i]
                    if S[i] != '-':
                        break
                    else:
                        S[i] = '+'
            times += 1
            happyside = S.count('+')
            if happyside == len(S):
                break
            # print "HappySide :: ", happyside

        print "Case #{}: {}".format(int(n+1), times)
        out.write("Case #{}: {}\n".format(int(n+1), times))
    file.close()
    out.close()

if __name__ == '__main__':
    RevengePancakes()

