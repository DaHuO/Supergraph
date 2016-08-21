#!/usr/bin/python

import sys

index = 1
T = int(input())
for case in range(0, T):
    print("Case #" + str(index), end=': ')
    index+=1

    n = int(input())
    outstr = ''
    lists = []
    flag = False
    for i in range(0, 2*n-1):
        lst = input()
        lists.append(lst.split())

    for l in lists:
        for i in range(0, len(l)):
            l[i] = int(l[i])

    while len(lists) != 1:
        lists = sorted(lists)
        odd_parity = []

        # two smallest lists first el should match
        if lists[0][0] != lists[1][0]:
            outstr += " " + str(lists[0][0])
            # match all lsts to lists[0]
            matchme = lists[0]
            lists.remove(lists[0])
            for i in range(1, len(matchme)):
                for l in lists:
                    if l[0] == matchme[i]:
                        lists.remove(l)
                        break
            lists = sorted(lists)
            for l in lists:
                outstr += " " + str(l[0])
            flag = True
            break
        else:
            checknums = []
            for el in lists[0]:
                checknums.append(el)
            for el in lists[1]:
                checknums.append(el)
            for i in range(2, len(lists)):
                checknums.append(lists[i][0])

            for xx in checknums:
                if xx in odd_parity:
                    odd_parity.remove(xx)
                else:
                    odd_parity.append(xx)

            assert(len(odd_parity) == 1)
            if len(odd_parity) != 1:
                print(odd_parity)
                for l in lists:
                    print(l)
            lists.remove(lists[0])
            lists.remove(lists[0])
            outstr += " " + str(odd_parity[0])


        for l in lists:
            l.remove(l[0])

    if flag == False:
        outstr += " " + str(lists[0][0])

    print(outstr.lstrip())
