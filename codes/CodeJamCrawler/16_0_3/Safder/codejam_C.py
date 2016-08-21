#! /usr/bin/python
import math,sys
def get_primes(limit):
	A = [2,3,5,7]
	l = 4
	for x in range(11,limit+1):
		sq = math.sqrt(x)
		f = 1
		for y in range(0,l):
			if ( x%A[y] == 0 ):
				f=0
				break
			if ( A[y] > sq ):
				f = 1
				break
		if f :
			A.append(x)
			l += 1
	return (A,l)
def is_prime(a,A,l):
	if ( a == 1):
		return (False,1)
	sq = math.sqrt(a)
	for x in range(0,l):
		if ( a%A[x] == 0 ):
			return (False,A[x])
		if ( A[x] > sq ):
			return (True,a)
	return (True,a)
def main():
	A,l=get_primes(65539)
	B = [ 0 for x in range(0,11) ]
	for x in range(1,11):
		B[x] = [ x**i for i in range(0,33) ]

	t = int(sys.stdin.readline())
	val1,val2=sys.stdin.readline().split()
	val1=int(val1)
	val2=int(val2)
	#for x in range(2,2**16+1):
	G=[]
	R=[]
	count = 0
	for x in range(2**(val1-1),2**(val1) + 1):
		val,res=is_prime(x,A,l)
		if ( count == val2):
			break
		if not val :
			st = str(bin(x))[2:]
			if ( st[-1] == '0' ):
				continue
			ans = 0
			f = 0
			G=[st]
			for j in range(2,11):
				ans = 0
				k = 0
				ll = len(st)
				for i in range(ll-1,-1,-1):
					if ord(st[i]) - 48:
						ans += B[j][k]
					k += 1
				res,val=is_prime(ans,A,l)
				if not res :
					G.append(val)
					f = 1
				else :
					f = 0
					G = []
					break;
			if f :
				R.append(G)
				count += 1
				
	case = 1
	print("Case #1:")
	for i in R:
		ans = i[0]
		for j in range(1,len(i)):
			ans += " "+ str(i[j])
		print(ans)	
	


if __name__=='__main__':
	main()
