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
findPrime()

tc = int(input())
s = input().split()
n = int(s[0])
j = int(s[1])

with open(str(n)+".txt") as f:
    mylist = f.read().splitlines()

print("Case #1:")
cnt = 0

for i in mylist:
	myStr = i
	print(myStr,end=" ")
	cnt_base=0
	for k in range(2,10+1):
		x = int(myStr,k)

		for num in primeList:
			if(x%num==0):
				print(num,end=" ")
				break
		cnt_base = cnt_base+1
	print()

	if(cnt_base!=9):
		print("Error Found")
		break
	cnt=cnt+1
	if(cnt==j):
		break
