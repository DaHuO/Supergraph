import itertools

def is_prime_or_factor(n):
	if n==2 or n==3:return 0 #actually can never get 0 bacause of nth and 1st mandatory 1 in jamcoin pattern
	if n<2 or n%2==0:return 2
	if n<9:return 0
	if n%3==0:return 3
	r=int(n**0.5)
	f=5
	while f<=r:
		if n%f==0:return f
		if n%(f+2)==0:return f+2
		f+=6
	return 0

def check(n,pcoin):
	proof=[0]*9
	for base in range(2,10+1):
		i=n-2
		value=1+(base**(n-1))		#parentheses important
		# print("initial:",value)
		for dig in pcoin:
			value+=(int(dig)*(base**i))
			i-=1
		test=is_prime_or_factor(value)
		# print(value)
		if test!=0:proof[base-2]=test
		else:return None					#prime in this BASE
	return proof 							#not prime in ALL BASES, so a JAMCOIN

def produce_jamcoins(n,j):
	count=0
	possible_jamcoins=list(itertools.product('01',repeat=n-2))
	for eachcoin in possible_jamcoins:
		prooflist=check(n,eachcoin)
		if prooflist!=None:
			print('1'+''.join(eachcoin)+'1',end=' ')
			for x in prooflist:print(x,end=' ')
			print()
			count+=1
			if count==j:return

tcases=int(input())
case=1
while case<=tcases:
	print('Case #'+str(case)+':')
	n,j=map(int,input().split())
	produce_jamcoins(n,j)
	case+=1