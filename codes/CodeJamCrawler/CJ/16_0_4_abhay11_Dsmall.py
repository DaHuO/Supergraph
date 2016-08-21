runs=int(input())
for run in range(runs):
	dat=input().split()
	k=int(dat[0])
	output=''
	for i in range(k):
		output+=' '+str(i+1)
	print('Case #'+str(run+1)+':'+output)
	