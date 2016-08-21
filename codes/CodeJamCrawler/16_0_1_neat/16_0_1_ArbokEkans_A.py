def f(n):
	if not n: return "INSOMNIA"
	s = set()
	curr = 0
	while len(s) < 10:
		curr+=1
		s |= set(str(curr*n))
	return curr*n

#for i in range(1, 10**6):
#	if f(i)//i >= 30:
#		print(i, f(i)//i)

for case in range(int(input())):
	print('Case #{}: {}'.format(case+1, f(int(input()))))