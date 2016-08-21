def solve(data):
	with open(data, 'rb') as f:
		with open('problem.out', 'wb') as sol:
			t = int(f.readline().strip())
			for i in range(1, t + 1):
				n = int(f.readline().strip())
				sol.write('Case #' + str(i) + ': ' + result(n) + '\n')

def result(num):
	if num == 0:
		return "INSOMNIA"
	array = [False] * 10
	curr = 0
	while True:
		curr += num
		for c in str(curr):
			d = int(c)
			array[d] = True
		if sum(array) == 10:
			return str(curr)
