
def done(l, n):
	while n > 0:
		l[n % 10] = 1
		n //= 10
	for i in l:
		if i == 0: return False
	return True

t = int(input())
for tc in range(t):
	n = int(input())
	l = [0] * 10
	ans = 'INSOMNIA'
	i = 1
	while n > 0:
		m = n * i
		if done(l, m):
			ans = str(m)
			break
		i += 1
	print ('Case #' + str(tc + 1) + ': ' + ans)