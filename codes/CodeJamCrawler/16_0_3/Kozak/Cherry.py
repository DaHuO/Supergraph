import math

count = int(input())
f = open('out.txt', 'w')
f.write("Case #1:\n")
lop = []
q = 1


def is_prime2(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return True

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(0,999):
        if n % lop[i] == 0:
            return lop[i]
    return True

while (True):
	q = q+2
	if is_prime2(q) == True:
		lop.append(q)
	if len(lop) == 1000:
		break

for i in range(0,count):
	stack = str(input())		
	NJ = stack.split()
	length = NJ[0]
	coins = NJ[1]
	x = 0
	workingNumbers = 0
	isDone = True
	while (isDone):
		divisors = [0,0,0,0,0,0,0,0,0]
		rawString = str(bin(x))[2:]
		bGroup = '1' + ("0"*(int(length)-(len(rawString)+2)))+ rawString + '1'
		works = True
		for j in range(2,11):
			divisors[j-2] = is_prime(int(bGroup,j))
			if divisors[j-2] == True:
				works = False;
				break
		if works == True:
			f.write(bGroup + " ")
			for j in range(0,9):
				f.write(str(divisors[j])+" ")
			f.write("\n")
			workingNumbers = workingNumbers + 1
		if workingNumbers == int(coins):
			isDone = False
		x = x + 2