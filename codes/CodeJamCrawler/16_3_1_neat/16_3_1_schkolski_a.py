filename = 'A-large.in'
import string
alpha = string.ascii_uppercase

def solve(arr, k):
	total = sum(arr)
	res = []
	
	minimum = min(arr)
	maksimum = max(arr)

	while maksimum != minimum:

		idx = -1
		for i in range(k):
			if arr[i] == maksimum:
				idx = i
				break

		res.append(alpha[idx])
		arr[idx] -= 1
		total -= 1
		maksimum = max(arr)

	if k % 2 != 0:
		idx = k - 1
		k -= 1

		while arr[idx] > 1:
			res.append(alpha[idx] + alpha[idx])
			arr[idx]-=2
			total -= 2
		if arr[idx] > 0:
			res.append(alpha[idx])
			arr[idx]-=1
			total-=1
		arr.pop(-1)


	while total != 0:

		for i in range(0, k, 2):
			if arr[i] > 0 and arr[i+1] >0:
				arr[i] -= 1
				arr[i+1] -= 1
				res.append(alpha[i]+alpha[i+1])

				total-=2


	return ' '.join([str(elem) for elem in res])



f = open(filename, 'r')
t = int(f.readline())
for i in range(t):
	k = int(f.readline())
	arr = [int(elem) for elem in f.readline().split()]


	print 'Case #{0}: {1}'.format(i + 1, solve(arr, k))
