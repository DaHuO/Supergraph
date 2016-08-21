#!/usr/bin/env python3

cases = int(input())

for i in range(cases):
	k, c, s = (int(x) for x in input().split(" "))
	print("Case #{}: {}".format(i + 1, " ".join([str(j + 1) for j in range(k)])))