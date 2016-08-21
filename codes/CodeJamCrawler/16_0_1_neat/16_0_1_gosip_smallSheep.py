def strToArr(n, l):
	arr = [0] * (10**(l+1))
	i = 0
	while n > 0:
		arr[i] = n % 10
		n = n // 10
		i += 1
	return arr

def arrToInt(arr, l):
	n = 0
	for i in range(l):
		n = n * 10 + arr[l-i-1]
	return n

def add(curr, arr, l):
	overflow = 0
	for i in range(l):
		s = curr[i] + arr[i] + overflow
		curr[i] = s % 10
		overflow = s // 10
	if overflow == 1:
		curr[l] = 1
		l += 1
	return l, curr

def countMax(n):
	if n == 0: return 'INSOMNIA'
	l = len(str(n))
	arr = strToArr(n, l)
	seen = [0] * 10
	curr = arr[:]
	while True:
		for	i in range(l):
			seen[curr[i]] = 1
		if sum(seen) == 10:
			break
		else:
			l, curr = add(curr, arr, l)
	return arrToInt(curr, l)

def main():
	f = open('A-large.in', 'r')
	t = int(f.readline())
	for i in range(t):
		n = int(f.readline())
		c = countMax(n)
		print('Case #' + str(i+1) + ': ' + str(c))

if __name__ == '__main__':
	main()