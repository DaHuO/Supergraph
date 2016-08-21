import math

N=32
J=500

primes=[2,3,5,7,11,13,17,19,23,29]

tot=N-2
res=[]
for i in range(2**tot):
	b= "1"+("{0:0"+str(tot)+"b}").format(i)+"1"
	divisors=[]
	for base in range(2,11):
		check=int(b,base)
		for prime in primes:
			if check%prime==0:
				divisors.append(prime)
				break
		if len(divisors)==base-1:
			continue
		break
	if len(divisors)==9:
		res.append([b]+list(map(str,divisors)))
		if len(res)==J:
			break

print("Case #1:")
for r in res:
	print(" ".join(r))



