#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def check_legal(sortedlist, parties):
    major = sortedlist[0][1]
    rest = 0
    for i in range(1,len(sortedlist)):
        rest += sortedlist[i][1]
    if major > rest:
        return False

    return True

def evacuate(sortedlist, parties):    
    if parties[sortedlist[0][0]] > 0:
        parties[sortedlist[0][0]] -= 1
        return sortedlist[0][0]
    return None

def is_all_evacuated(parties):
    for k in parties:
        if parties[k] != 0:
            return False
    return True

def solve(N, senators):
    parties = {}
    evacuated = []
    nm = ord('A')
    for n in senators:
        parties[chr(nm)] = n
        nm += 1

    while True:
        e1 = evacuate(sorted(parties.items(), key=lambda x:x[1], reverse=True), parties)
        if is_all_evacuated(parties):
            evacuated.append(e1)
            break

        e2 = evacuate(sorted(parties.items(), key=lambda x:x[1], reverse=True), parties)
        if check_legal(sorted(parties.items(), key=lambda x:x[1], reverse=True), parties):
            evacuated.append(e1+e2)
        else:
            evacuated.append(e1)
            parties[e2] += 1
        if is_all_evacuated(parties):
            break

    return ' '.join(evacuated)

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        N = int(f.readline())
        senators = map(int, f.readline().rstrip().split())
        answer = solve(N, senators)

        print "Case #%d: %s" % (i+1, answer)

# sort by key
# for k,v in sorted(d.items())
# sort by value
# for k,v in sorted(d.items(), key=lambda x:x[1])
# items() return tapple, tapple[0] is k, tapple[1] is v
#
# import copy
# copy.copy()
# copy.deepcopy()
#
# a = [0]*100
#
# for tc in xrange(1, int(sys.stdin.readline())+1):
#   A, B = [int(w) for w in sys.stdin.readline().split()]
#   p = [float(w) for w in sys.stdin.readline().split()]
#
# array = [[0 for j in range(m)] for i in range(n)]

