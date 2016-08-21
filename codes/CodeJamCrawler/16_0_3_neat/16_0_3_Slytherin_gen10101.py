file = open("dummy.txt","w")
file.close()
nPossible = 0
primeList=[]
def findPrime():
	global primeList
	for i in range(2,26384):
		isPrime=True
		for j in primeList:
			if(i%j==0):
				isPrime=False
		if(isPrime):
			primeList.append(i)
def check(n):
	for i in primeList:
		if(n%i==0):
			return True
	return False

def genJamCoin(jamStr,index,n):
	global nPossible
	global primeList
	if(nPossible <= int(500) ):

		if(index==n):
			jamStr=jamStr+"1"
			isJam = True

			for i in range(2,10+1):
				jamInt = int(jamStr,i)
				if(not check(jamInt)):
					isJam = False
					break

			if(isJam):
				print(jamStr)
				file.write(jamStr+"\n")
				nPossible=nPossible+1

		else:
			genJamCoin(jamStr+"0",index+1,n)
			genJamCoin(jamStr+"1",index+1,n)

findPrime()
for i in range(0,32):
	nPossible = 0
	file = open(str(i+2)+".txt","w")
	genJamCoin("1",0,i)
	file.close()
print(len(primeList))
