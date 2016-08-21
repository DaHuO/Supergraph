import math 

def isPrime(n):
	i = 2
	while(i <= int(math.sqrt(n))):
		#print('i: %d' % i)
		if(n % i == 0):
			return False
		i += 1
	return True;

def isJamCoin(L):
#	print("ebter")
	for x in L:
#		print(x)
		if(isPrime(x)):
			return False;
	return True;

def fillNt_Div(L, NTD):
	for x in L:
		for y in range(2, x):
			if(x % y == 0):
				NTD.append(y);
				break;
	
T = int(input())
N = 16
J = 50

print("Case #1:");
i = 0
base = pow(10, 14);
addend = 0;
p = 0;
base_int = list()
nt_div = list()

while(i < J):
	base_int = []
	nt_div = []
	n = int(str(base + addend)+'1')
#	print('n: '+str(n))
	base_int = [int(str(n), x) for x in range(2, 11)]
#	print('basint: %r' % base_int)
	jamcoin = isJamCoin(base_int);
#	print(jamcoin)
	if(jamcoin):
		print('%d\t' % n , end="")
		fillNt_Div(base_int, nt_div);
	#	print('size: %d' % len(nt_div))
		for y in nt_div:
			print('%d\t' % y, end="");
		i += 1
		print()
	addend = int(bin(p + 1)[2:]);
#	print('add: '+str(addend))
	p += 1