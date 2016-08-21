n = int(input())

def answer(N):
	if N == 0: 
		return "INSOMNIA"
	digits = set()

	curNum = N
	digits = digits.union(set(str(curNum))) 
	while len(digits) < 10:
		curNum += N 
		digits = digits.union(set(str(curNum))) 
		# print(digits, curNum)
	return str(curNum)

for i in range(n):
	M = int(input())
	print(("Case #%d: " % (i+1)) + answer(M))