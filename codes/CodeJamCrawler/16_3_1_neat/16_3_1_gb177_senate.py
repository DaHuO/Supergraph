#!/usr/bin/python

from heapq import *

def Nr(): return tuple(map(int, raw_input().split()))

T = Nr()[0]
for t in range(1, T + 1):
    N = Nr()[0]
    S = Nr()

    def add(l1, l2):
        return chr(ord('A') + l1) + chr(ord('A') + l2)

    def add1(l1):
        return chr(ord('A') + l1)

    answer = []
    room = [(s, i) for i, s in enumerate(S)]
    room.sort(reverse= True)
    while sum(s for s, i in room) > 0:
        # print room
        if len(room) == 2:  # two parties left
            if room[0][0] > room[1][0]:
                answer.append(add1(room[0][1]))
            for i in range(room[1][0]):
                answer.append(add(room[0][1], room[1][1]))
            break
        else:
            sb, lb = room[0]
            answer.append(add1(lb))
            if sb > 1:
                room[0] = sb-1, lb
            else:
                del room[0]

        room.sort(reverse= True)


    print "Case #%d: %s" % (t, " ".join(answer))

