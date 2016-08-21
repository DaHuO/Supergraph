T = int(input())
for t in range(T):
	res = 'INSOMNIA'
	n = int(input())
	if n != 0:
		st = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
		k = n
		while st:
			for c in str(k):
				if int(c) in st:
					st.remove(int(c))
			res = k
			k += n
	print('Case #{}: {}'.format(t + 1, res))