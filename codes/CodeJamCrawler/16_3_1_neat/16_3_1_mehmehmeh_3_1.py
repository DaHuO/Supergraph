f = open('input.txt')
n = int(f.readline())

out = open('output.txt', 'w')

for i in range(n):
	res = 'Case #' + str(i+1) + ': '
	num = int(f.readline())

	nums = f.readline().split()

	hsh = [[int(nums[j]), chr(65 + j)] for j in range(num)]
	sm = reduce(lambda x, y: int(x) + int(y), nums)

	while sm > num:
		hsh.sort(reverse = True)
		ko = 0
		for z in range(num):
			if hsh[z][0] == hsh[0][0]:
				ko+=1
		print ko
		if ko % 2 == 0:
			res += hsh[1][1]
			hsh[1][0] -= 1
			sm -=1
		res += hsh[0][1] + ' '
		hsh[0][0] -= 1
		sm -=1

	if num % 2 != 0:
		res += hsh[-1][1] + ' '
	for k in range(num / 2):
		res += hsh[2 * k][1] + hsh[2 * k + 1][1] + ' '
	out.write(res + '\n')