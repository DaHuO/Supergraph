import time
def checkprime(x):
	#print(x,'cprime')
	for i in range(2,int(x**0.5)+1):
		if(x%i==0): return i
	return 1

def check(s):
	global ans
	global J
	global count
	if(len(ans)<J):
		#print(count)
		count+=1
		#print(type(s[0]))
		number = ''.join(s)
		tempans=[]
		for base in range(2,10,1):
			x = checkprime(int(number,base))		
			if(x>1): tempans.append(x)
		#	print(x,'x')


		x = checkprime(int(number))
		if(x>1): tempans.append(x)
		#print(x,'x')

		if(len(tempans)==9): ans[number]=tempans

def generator(s,i):
	global ans
	global J
	if(len(ans)==J): return
	if(i==0):
		check(s)
	else:
		s[i]='0'
		generator(s,i-1)
		s[i]='1'
		generator(s,i-1)

def main():
	clock = time.clock()
	T = int(input())
	global J
	N,J = [int(x) for x in input().split()]
	s = '1'+'0'*(N-2)+'1'
	sl=list(s)
	global ans
	ans = {}
	global count
	count =0
	generator(sl,N-2)
	for key in ans.keys():
		print(key,' '.join([str(x) for x in ans[key]]))
	#print(time.clock()-clock)


main()