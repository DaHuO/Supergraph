



primeTable=[]
primeSet=set()

def isPrime(n) :
	if n==2 : return True
	if n==1 or n%2==0 : return False
	for prime in primeTable :
		if prime*prime>n :
			return True
		if n%prime == 0 : return False


for i in range(65600) :
	if isPrime(i) : 
		primeTable.append(i)
		primeSet.add(i)

r=input()

(length, nJamCoin)=map(lambda x:int(x),input().split(" "))

found=0
for i in range(2**(length-1)+1, 2**length,2) :
	if found == nJamCoin : break
	divisors=[]
	for j in range(2,11):
		n=int(bin(i)[2:],j)
		# print("testing : "+str(n))
		if n in primeSet : break
		for prime in primeTable :
			if n % prime == 0 :
				divisors.append(prime)
				break

	# print(divisors)
	if len(divisors)==9:
		found+=1
		print(str(bin(i))[2:]+" "+str(divisors)[1:-1].replace(',',''))