#Code Jam problem "Fractiles" Qualification Round 2016
#https://code.google.com/codejam/contest/6254486/dashboard
#-Thomas Steinke codejam@thomas-steinke.net 2016-04-08
import sys

T = int(sys.stdin.readline())
for t in range(T):
	kcs = sys.stdin.readline().split()
	k = int(kcs[0])
	c = int(kcs[1])
	s = int(kcs[2])
	assert s == k
	ans = "Case #" + str(t+1) + ":"
	for i in range(k): ans = ans + " " + str(i+1)
	print ans
