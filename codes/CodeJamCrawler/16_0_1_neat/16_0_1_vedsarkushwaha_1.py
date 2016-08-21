def fun(lst):
	for i in range(10):
		if(lst[i]==0):
			return True
	return False

def addToLst(lst, N):
	while(N!=0):
		lst[N%10]=1
		N=N/10;
	return lst

if __name__=="__main__":

	T = int(raw_input())
	for j in range(T):
		lst = [0]*10
		N = int(raw_input())
		if(N==0):
			print "Case #%d: INSOMNIA" % (j+1)
		else:
			i=1
			while(fun(lst)):
				lst = addToLst(lst,N*i)
				i+=1
			print "Case #%d: %d" % ((j+1),N*(i-1))