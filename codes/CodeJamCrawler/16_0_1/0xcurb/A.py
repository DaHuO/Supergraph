def main():
	T = input()
	for i in range(T):
		seen = []
		N = input()
		if not N:
			print 'Case #{0}: INSOMNIA'.format(i+1)
			continue

		j = 1
		while len(seen)<10:
			n = j*N
			last = n
			while n>0:
				d = n%10
				if d not in seen:
					seen.append(d)
				n /= 10
			j += 1

		print 'Case #{0}: {1}'.format(i+1, last)

main()