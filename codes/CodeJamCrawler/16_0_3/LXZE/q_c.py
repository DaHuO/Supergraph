import cPickle
from math import sqrt, fmod;
from itertools import count, islice
primes_list = cPickle.load(open('primes_16.txt', 'rb'))
f = open("in_q_c.in","r")
w = open("output_c.txt","w")
num = f.readline()

def convert(input, source, target):
	if source == target: return input
	base = {
		2 :'01',
		3 :'012',
 		4 :'0123',
		5 :'01234',
		6 :'012345',
		7 :'0123456',
		8 :'01234567',
		9 :'012345678',
		10 :'0123456789',
		}
	baseSrcList = base[source]
	baseSrc = len(baseSrcList)
	baseTargetList = base[target]
	baseTarget = len(baseTargetList)
	data = 0
	if baseSrc != 10:
		i = 0
		for iDigit in list(str(input)[::-1]):
			data += baseSrcList.index(iDigit)*pow(baseSrc,i)
			i+=1
	else : data = input

	if baseTarget != 10:
		tempInput = int(data)
		t = ''
		if tempInput == 0: t+=baseTargetList[0]
		while tempInput != 0:
			t += baseTargetList[tempInput%baseTarget]
			tempInput/=baseTarget
		return t[::-1]
	else:
		return str(data)

isPrime = lambda n:n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def factors(n):    
	tmp = 0
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			# tmp = i if i != 2 else n//i
			tmp = i
			break
	return str(tmp)

for it in range(0,int(num)):
	N,J = [int(l) for l in f.readline().split()]
	length = 0
	res = '\n'
	for i in range(2,2**N):
		ret = convert(i,10,2)
		if ret[0] == '1' and ret[-1] == '1' and len(ret) == N:
				l = [long(convert(ret,base,10)) for base in range(2,11)]
				if not True in map(isPrime,l):
					tmp = ret +' '+ ' '.join(map(factors,l)) + '\n'
					print tmp
					res += tmp
					length+=1
		if length == J:
			break
	print("Case #{0}: {1} ".format(it+1,res))
	w.write("Case #{0}: {1}\n".format(it+1,res))
w.close()