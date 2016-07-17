def gnomesort(seq):
	i = 1
	while i < len(seq):
		if i == 0 or seq[i - 1] < seq[i]:
			i += 1
		else:
			seq[i - 1], seq[i] = seq[i], seq[i - 1]
			i -= 1

seq = [23, 2, 1, 3, 4, 5, 6, 20, 11, 12]
gnomesort(seq)
print seq