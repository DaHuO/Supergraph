def flip(s):
	t = []
	for i in s:
		if i == '+':
			t += ['-']
		else:
			t += ['+']
	return "".join(t)


def solve(s):
	res = 0
	i = len(s) - 1
	while (i >= 0):
		if s[i] == '-':
			s = flip(s)
			res += 1
		i -=1

	return res


f = open("intput.txt", "r")
n = int(f.readline())


for i in range(n):
	s = f.readline()
	print("Case #" + str(i+1) + ": " + str(solve(s)))
# import math 

# n = 6
# j = 11

# def toI(n, i):
# 	res = 0
# 	base = 1
# 	l = len(n)
# 	for j in range(l):
# 		res += int(n[l-j-1]) * base
# 		base *= i
# 	return res

# def isPrime(n):
# 	for i in range(2, int(math.sqrt(n)) +1 ):
# 		if n % i == 0:
# 			return i
# 	return 0
			
# def check(n):
# 	# n == str 01101010
# 	res = []
# 	for i in range(2, 11):
# 		t = toI(n, i)
# 		#print(n, " to ", i, " is ", t)
# 		r = isPrime(t)
# 		if r == 0:
# 			return False, 0
# 		else:
# 			res += [r]
# 	return True, res

# ans = []
# div = {}
# cnt = 0
# for i in range(2**n + 1, 2**(n+1)-1):
# 	s = bin(i)[2:].zfill(n)
# 	if not( s[n] == '1'):
# 		continue
# 	r, t = check(s)
# 	if r==True:
# 		ans += [s]
# 		div[s] = t
# 		cnt += 1
# 		print "+1"
# 	if cnt == j:
# 		break

# print("Case #1:")
# for i in range(j):
# 	ress = " ".join([str(x) for x in div[ans[i]]])
# 	print(ans[i] + " " +  ress)