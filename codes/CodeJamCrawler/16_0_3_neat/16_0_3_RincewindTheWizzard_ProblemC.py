import math

bases = list(range(2,11))
N = 16
jamlen = 16
J = 50
radixes = []

for b in bases:
	radixes.append([])
	for n in range(N):
		radixes[b-2].append(int(math.pow(b, n)))

def isPrime(n):
	for i in range(2,int(math.sqrt(n))+ 1):
		if (n%i == 0):
			return i
	return -1


def baseToDec(num,base):
	if base == 10:
		return num

	num = [int(x) for x in str(num)]
	num = num[::-1]
	temp = 0;
	for i in range(len(num)):
		temp += num[i]*radixes[base - 2][i]
	return temp

def isJamcoin(j):
	for b in bases:
		if(isPrime(baseToDec(j,b)) == -1):
			return False
	return True

out = ''
start = [1]

jamcoins = []


for i in range(0, int(math.pow(2,N-2))):
	divs = []
	binum = bin(i)
	binum = [int(x) for x in str(binum)[2:]]

	binum.insert(0, 1)
	binum.append(1)
	print(len(binum))
	if(len(binum) > jamlen):
		break
	elif(len(binum) < jamlen):
		continue

	binum = int(''.join(map(str,binum)))
	print(binum)

	for b in bases:
		div = isPrime(baseToDec(binum,b))
		if (div != -1):
			divs.append(div)
		else:
			break
	if(len(divs) == 9):
		
		jamcoins.append(str(binum) + ' ' + ' '.join(str(x) for x in divs))

	

	if(len(jamcoins) >= J):
		break

o = open("outfile.txt",'w')
out = ''


out += 'Case #1:\n'
out +='\n'.join(jamcoins)

o.write(out)
o.close()

print('\n'.join(jamcoins))


# print(radixes[0][0])
# print(radixes[0][1])
# print(radixes[0][2])
# print(radixes[0][3])
# print()

# print(radixes[1][0])
# print(radixes[1][1])
# print(radixes[1][2])
# print(radixes[1][3])

