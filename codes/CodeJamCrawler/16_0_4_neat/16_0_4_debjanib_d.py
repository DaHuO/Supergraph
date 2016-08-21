import string

T = int(raw_input())
for t in range(T):
	K, C, S=map(int, raw_input().split())
	s = ""
	for i in range(1, K+1):
		s += str(i)+" "
	print ("Case #%d: %s" % (t+1, s))