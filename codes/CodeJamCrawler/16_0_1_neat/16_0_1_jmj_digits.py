
def count(n):
	digits_seen = set(range(0, 10))
	multiply = 0
	while(digits_seen):
		multiply += 1
		current = n * multiply
		for char in str(current):
			digits_seen.discard(int(char))
		
	return(n * multiply)



testcases = int(input())
for test in range(0,testcases):
	n = int(input())
	if (n == 0):
		print("Case #%d: INSOMNIA" %(test + 1))
	else:
		print("Case #%d: %d" %(test + 1, count(n)))
