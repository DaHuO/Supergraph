from sets import Set
f = open('A-large.in','r')
out = open('outputLarge.txt','w')

def CountingSheep(n):
	digits = Set()
	if(n == 0): 
		return "INSOMNIA"
	s = str(n)
	for i in s:
		digits.add(i)
	if len(digits) == 10:
		return n
	cnt = 1
	while(len(digits) != 10):
		cnt += 1
		num = cnt*n
		s = str(num)
		for i in s:
			digits.add(i)
	return num

tests = f.readline()
for i in range(1,int(tests)+1):
	num = int(f.readline())
	ans = CountingSheep(num)
	out.write("Case #"+str(i)+ ": "+str(ans)+"\n")