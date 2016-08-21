def decompose(n):
	l = []
	while n > 0:
		l.append(n%10)
		n //= 10
	l.reverse()

	return l

def solve(n):
	if n == 0:
		return "INSOMNIA"

	track, x = [0 for i in range(10)], 0
	while True:
		x += 1
		for y in decompose(x*n):
			track[y] = 1
		exiting = True
		for z in track:
			if z == 0:
				exiting = False
				break

		if exiting:
			break
	
	return x * n

t = int(input())
for cc in range(t):
	n = int(input())
	
	print("Case #{}: {}".format(cc+1, solve(n)))
