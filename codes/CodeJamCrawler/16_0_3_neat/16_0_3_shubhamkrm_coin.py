import math

def convert(num,base):
	rev=1
	output=0
	while(num>0):
		digit = num%base;
		rev = rev*10+digit
		num/=base
	while (rev>0):
		digit = rev%10
		output = output*10+digit
		rev/=10
	output/=10
	return output

def interpret(num,base):
	i=0
	output = 0
	while (num>0):
		output+=(num%10)*(base**i)
		i+=1
		num/=10
	return output

def isPrime(num):
	i=2
	while i<=int(math.sqrt(num)):
		if (num%i==0):
			return 0
		i+=1
	return 1


def main():
	bases = [2,3,4,5,6,7,8,9,10]
	t = input()
	for i in range(t):
		print "Case #%d:"%(i+1)
		n,j = raw_input().split()
		n = int(n)
		j = int(j)
		count_primes=0
		num  = (1<<(n-1))+1
		upper_limit = 1<<n
		while num<upper_limit and count_primes<j:
			proofs = [0]*9
			count_factors=0
			if (isPrime(num)==0):
				num2=convert(num,2)
				for base in bases:
					new_num=interpret(num2, base)
					k=2
					while (k<=math.sqrt(new_num)):
						if (new_num%k==0):
							proofs[base-2]=k
							break
						k+=1
			for proof in proofs:	
			    if proof>0:
			    	count_factors+=1
			if count_factors==9:
			    count_primes+=1
			    print convert(num,2),
			    for proof in proofs:
			    	print proof,
			    print
			num+=2

main()
