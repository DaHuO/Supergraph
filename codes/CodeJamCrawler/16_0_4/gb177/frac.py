#!/usr/bin/python

#
# for S=K, this should be easy - just test all positions K
#

T = int(raw_input())
for c in range(T):
    K, C, S = map(int, raw_input().split())
    pos = sum(K**i for i in range(C))
    l = [1 + pos * i for i in range(S)]
    print "Case #%d: %s" % (c+1, " ".join(map(str, l)))
