filename = "A-large"
infile= filename + '.in'
f = open(infile)
inp = f.readlines()
f.close()
outfile = filename + '.out'
f = open(outfile,'w')
case = int(inp.pop(0))
for case in range(1, case + 1):
	N = inp.pop(0)
	L = list(map(int, inp.pop(0).split()))
	Party = list(map(chr, range(65, 91)))
	num = sum(L)
	S = str()
	m = max(L)
	max_list = [i for i, j in enumerate(L) if j == m]
	print(L[max_list[0]])
	while num > 0:
		if len(max_list) %2 == 1:
			S += Party[max_list[0]]
			L[max_list[0]] -= 1
		else:
			S += Party[max_list[0]]
			S += Party[max_list[1]]
			L[max_list[0]] -= 1
			L[max_list[1]] -= 1
		S += ' '
		num = sum(L)
		m = max(L)
		max_list = [i for i, j in enumerate(L) if j == m]
	print(S)
	print('Case #{}: {}'.format(case, S))
	f.write('Case #{}: {}\n'.format(case, S))
f.close()	
