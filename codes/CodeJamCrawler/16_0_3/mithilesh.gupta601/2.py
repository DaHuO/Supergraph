import time


def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return [True,1]
    if n == 3:
        return [True,1]
    if n % 2 == 0:
        return [False,2]
    if n % 3 == 0:
        return [False,3]
    i = 5
    w = 2

    while i * i <= n:
        if i>10000000:
            return [True,1]
        if n % i == 0:
            return [False,i]

        i += w
        w = 6 - w

    return [True,1]

def toBase(n,b):
	dec=bin(n)[2:]
	return int(dec,b)
	
start = time.time()

f = open('prime.txt', 'w')
f2 = open('out.txt', 'w')
c=0
exc=[2147483671,2147483699,2147483675,2147483657,2147483687,2147483701,2147483711,2147483729,2147483731,2147483761,2147483773,2147483787,2147483789,2147483803,2147483807,2147483809,2147483817]
#for i in range(2147483649,4294967296,2):
for i in range(2147483807,4294967296,2):

	if i in exc:
		continue
	if c>500:
		break
	currList=[]
	lis = isprime(i)
	print(i,lis)

	if lis[0]:
		continue
	currList.append(str(lis[1]))
	b3=0
	flag=0
	for j in range(3,11):
		b3=toBase(i,j)
		lis = isprime(b3)
		print(i,j,lis)
		if lis[0]:
			flag=1
			break
		currList.append(str(lis[1]))
	if flag==0:
		c+=1
		f.write(str(i)+","+bin(i)[2:]+":"+' '.join(currList)+"\n")
		f2.write(bin(i)[2:]+" "+' '.join(currList)+"\n")
	print(str(i)+",count="+str(c)+"\n")
		
f.close()
f2.close()
end = time.time()
print(end - start)
