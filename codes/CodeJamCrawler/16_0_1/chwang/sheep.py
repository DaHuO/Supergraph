
def count(N):
	if N == 0:
		return -1
	counted = [0] * 10

	i = 1
	while sum(counted) < 10:
		num = N * i
		for c in str(num):
			counted[int(c)] = 1
		i = i + 1

	return num


with open('A-large.in') as f_in:
	T = int(f_in.readline())
	nums = f_in.read().split('\n')

with open('A-large.out', 'w') as f_out:
	for i in range(T):
		result = count(int(nums[i]))
		f_out.write('Case #' + str(i+1) + ': ')
		if result == -1:
			f_out.write('INSOMNIA\n')
		else:
			f_out.write(str(result) + '\n')

