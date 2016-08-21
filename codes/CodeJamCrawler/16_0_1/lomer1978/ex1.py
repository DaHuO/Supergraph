import sys
[T]=[int(i) for i in sys.stdin.readline().split()]
for i in range(T):
	print ("Case #" + "{}".format(i+1) + ": ", end="")
	[N]=[int(i) for i in sys.stdin.readline().split()]
	if N==0:
		print("INSOMNIA")
	else:
		dcount=0
		dshown=[0]*10
		dstep=0
		curnum=0
		while True:
			dstep=dstep+1
			curnum=N*dstep
			for ch in str(curnum):
				if dshown[int(ch)]==0:
					dshown[int(ch)]=1
					dcount=dcount+1
			if dcount==10:
				break
		print(curnum)
