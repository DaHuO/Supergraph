def check(n):
	if n==0:
		return "INSOMNIA"
	i = n
	digits = [0,0,0,0,0,0,0,0,0,0]
	while digits.count(1)<10:
		for d in getDigits(n):
			digits[d]=1
		n += i
	return n-i

def getDigits(n):
	return [int(d) for d in str(n)]

f = open('A-small-attempt0.in','r')
small = f.read().split('\n')[1:-1]
f.close()
case = 1

for x in small:
	print("Case #"+str(case)+": "+str(check(int(x))))
	case += 1

f = open('A-large.in','r')
large = f.read().split('\n')[1:-1]
f.close()
case = 1

for x in large:
	print("Case #"+str(case)+": "+str(check(int(x))))
	case += 1
