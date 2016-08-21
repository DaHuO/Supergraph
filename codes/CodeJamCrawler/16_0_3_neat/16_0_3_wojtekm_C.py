from __future__ import print_function

J = 500
N = 32

def convert(s, base):
	mul = 1
	res = 0
	
	for i in reversed(s):
		res += (ord(i)-ord('0'))*mul;
		mul *= base
	
	return res
	
def generate(x):
	s = ""
	while x != 0:
		s = chr(x%2 + ord('0')) + s
		x /= 2
	
	while len(s) < N-2:
		s = "0"+s
		
	return "1"+s+"1"
	
def findDivisor(a):
	i = 2
	while i*i*i*i*i*i <= a:
		if a%i == 0:
			return i
		i+=1
	
	return 0
	
print("Case #1:")
x = 1
numOfRes = 0

while numOfRes != J:
	s = generate(x)
	ok = True
	div = []
	for i in range(2, 11):
		tmp = findDivisor(convert(s, i))
		if tmp != 0:
			div.append(tmp)
		else:
			ok = False
			break
	
	if ok:
		print(s+" ", end="")
		for i in div:
			print(str(i)+" ", end="")
		print("")
		numOfRes += 1
		
	x += 1
