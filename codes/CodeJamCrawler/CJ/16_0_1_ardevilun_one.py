import sys

def fn(N,arr):
	while(N):
		if N%10 in arr:
			pass
		else:
			arr.append(N%10)
		N=N/10

T=int(sys.stdin.readline())
for a in range(1,T+1):
	arr=[]
	N=int(sys.stdin.readline())
	if N == 0:
		print "Case #"+str(a)+": INSOMNIA"
	else:
		count = 0
		while(len(arr) != 10):
			count+=1
			fn(count*N,arr)


		print "Case #"+str(a)+": "+str(count*N)


