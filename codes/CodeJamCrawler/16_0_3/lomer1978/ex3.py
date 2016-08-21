import sys
[T]=[int(i) for i in sys.stdin.readline().split()]
for i in range(T):
	print ("Case #" + "{}".format(i+1) + ":")
	[N, J]=[int(i) for i in sys.stdin.readline().split()]
	for j in range(J):
		if N==16:
			baseN="1"+"{0:0>6b}".format(j)+"1"
		else:
			baseN="1"+"{0:0>14b}".format(j)+"1"
		line=""
		line2=""
		for k in range(2):
			line=line+baseN
		for k in range(9):
			div=int(baseN, k+2)
			line2=line2+" {}".format(div)
		print(line, line2)
