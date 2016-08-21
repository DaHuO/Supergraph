t=int(input())
for i in range(t):
	sequence=input()
	count=0
	firstValue=sequence[0]
	length=len(sequence)
	for j in range(length):
		if(sequence[j]!=firstValue):
			count=count+1
			firstValue=sequence[j]
	if(sequence[length-1]=='-'):
		count=count+1
	print("Case #"+str(i+1)+": "+str(count))