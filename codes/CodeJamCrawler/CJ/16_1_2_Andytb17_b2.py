def find_missing_numbers(ls):
	seen = dict()
	for num in ls:
		if num in seen:
			seen[num] += 1
		else:
			seen[num] = 1
	result = list()
	for num in seen.keys():
		if seen[num]%2 == 1:
			result.append(num)
	return sorted(result)
def solve(f_in, f_out):
	fin  = open(f_in)
	fout = open(f_out,'w')
	num_case = int(fin.readline().strip())
	for i in xrange(num_case):
		N = int(fin.readline().strip())
		nums = list()
		for j in xrange(2*N-1):
			line = fin.readline().strip()
			nums.extend( [int(a) for a in line.split(' ')])
		missing = find_missing_numbers(nums)
		fout.write('Case #'+str(i+1)+':')
		for m in missing:
			fout.write(' '+str(m))
		fout.write('\n')
	fin.close()
	fout.close()
solve('B-large.in.txt','out_big.txt')
