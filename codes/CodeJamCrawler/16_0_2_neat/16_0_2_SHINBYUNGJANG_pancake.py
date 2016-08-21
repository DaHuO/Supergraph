c=int(raw_input())
count=0
for i in range(c):
	pan=raw_input()
	times=0
	pan=list(pan)
	for j in range(len(pan)-1):

		if pan[j]!=pan[j+1]:
			times=times+1
			for k in range(j):
				pan[k]=pan[j+1]

	if pan[len(pan)-1]=="-" :
		times=times+1
	print "Case #"+str(i+1)+": "+str(times)
