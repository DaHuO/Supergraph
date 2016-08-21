import sys

k = 1
ans = [0]*11;

powers = []
powers.append([])
powers.append([])

def pre():
	for x in xrange(2,11):
		arr = [1]
		for y in xrange(1,32):	
			arr.append(arr[y-1] * x)
		powers.append(arr)		

def getfactor(j):
	for i in xrange(2,sys.maxint):
		if(i * i > j):
			break
		if(j % i == 0):
			return i;
	return -1;

def setBit(mask, i):
	return (mask | (1<<i))

def checkBit(mask, i):
	return (mask & (1<<i));

def check(mask, base, n):
	ret = 0
	if(base == 2):
		ret = mask
	else:
		for x in xrange(0,n):
			if(checkBit(mask,x)):
				ret += powers[base][x]
	factor = getfactor(ret)
	if(factor != -1):
		ans[base] = factor
		return 1
	return 0
			

def solve(k):

	print "Case #"+str(k)+":"
	k += 1
	n, p = map(int, raw_input().split())
	mask = 1;
	mask = setBit(mask, n-1);

	count = 0
	flag = 1
	for i in xrange(mask, sys.maxint, 2):
		flag = 1
		if count == p:
			break
		for j in xrange(2,11):
			if(not check(i,j,n)):
				flag = 0
				break
		if(flag):
			print bin(i)[2:],
			for x in xrange(2,11):
				print ans[x],
			print
			count += 1
	return k

def main():
	pre()
	t = int(raw_input());
	k = 1
	while(t!=0):
		k = solve(k)
		t -= 1
	
main()
