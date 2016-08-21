t = input()
for case in range(0,t):
	num = map(int,raw_input().split())
	K = num[0]
	C = num[1]
	S = num[2]
	print "Case #%d: "%(case+1),
	for i in range(1,K+1):
		print i," ",
	print
