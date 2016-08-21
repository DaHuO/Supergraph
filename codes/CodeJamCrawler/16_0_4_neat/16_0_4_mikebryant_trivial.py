#!/usr/bin/env python

T = int(raw_input().strip())

for i in range(1, T+1):
    print ("Case #%d:" % i),
    K, C, S = [int(x) for x in raw_input().strip().split()]

    assert K == S

    print ' '.join([str(x) for x in range(1, K+1)])
