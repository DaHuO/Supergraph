def f(inp):
	K, _, _ = [int(x) for x in inp.split()]
	return ' '.join(str(x) for x in range(1, K+1))

#for i in range(1, 10**6):
#	if f(i)//i >= 30:
#		print(i, f(i)//i)

for case in range(int(input())):
	print('Case #{}: {}'.format(case+1, f(input())))