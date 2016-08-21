def finddigits(n,digarray):
	dig=str(n)
	for ch in dig:
		d=int(ch)
		digarray[d]=d
		if iscomplete(digarray,10):
				return 1
	return 0

def iscomplete(digarray,n):
	i=0
	for i in range(n):
		if i not in digarray:
			return 0
	return 1

def asleep(n,seq):
	i=2
	number=n
	#print(number)
	digarray=[-1]*10
	if n==0:
		print("Case #"+str(seq)+": "+"INSOMNIA")
		return
	if n==1:
		print("Case #"+str(seq)+ ": " +"10")
		return

	while(True):
		
		if finddigits(n,digarray)==1:
			print("Case #"+str(seq)+": "+str(n))
			return
		n=i*number;
		
		i=i+1
		

#main program
n=int(input())
i=1;
while(n>0):
	num=int(input())
	asleep(num,i)
	n=n-1
	i=i+1