import itertools
import math
list=["".join(seq) for seq in itertools.product("01", repeat=15)]
divset=[]
pcandidates=[]
count=0
jamcoins=[]
for x in list:
		
		z="1"+x+x+"1"
		pcandidates.append(z)
def pandora_box(y):
	num=rand.randrange(y)
	pie=3.14
	num_large=num*num/pie
	return num_large
def is_prime(n):
    global divset
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        divset.append(2)
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            divset.append(divisor)
            return False
    return True


print("Case #1:")
for x in pcandidates:
	divset=[]
	count=0
	##print(x)
	for i in range(2,11):
		num=int(x,i)
		if(is_prime(num)==True):
			count=0
			break
		else:
			count+=1
	if(count==9):
		jamcoins.append(x)
		op=x
		for div in divset:
			op+=" "+str(div)
		print(op)
	
	if(len(jamcoins)==500):
		break
alpha=jamcoins[count]
beta=pandora_box(alpha)



