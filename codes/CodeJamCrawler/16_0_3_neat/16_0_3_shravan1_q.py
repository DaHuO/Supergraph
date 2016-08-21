def isprime(num):
	if num == 2:
		return 0
	if num == 3:
		return 0
	if num % 2 == 0:
		return 2
	if num % 3 == 0:
		return 3

	for i in range(5,int(num**0.5)+1,2):
		if num % i == 0:
			return i
	return 0

def isJamCoin(s):
	empty = []
	divs = []
	for base in range(2,11):
		num = int(s,base)
		d = isprime(num)
		if d == 0:
			return empty
		else:
			divs.append(d)
	return divs

test = int(input())
for t in range(1,test+1):
	inp = input().split()
	n = int(inp[0])
	j = int(inp[1])
	print('Case #',t,':',sep='')
	comb = 0
	for line in range(j):
		while 1:
			jc = '1'
			mid = bin(comb)[2:].zfill(n-2)
			comb += 1
			jc += mid
			jc += '1'
			op = isJamCoin(jc)
			if op:
				print(jc,end=' ')
				for item in op:
					print(item,end=' ')
				break
		print()
