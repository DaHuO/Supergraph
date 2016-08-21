import sys

def flip_pc(pc):
	count = 0
	r = pc
	while True:
		ok = True
		for c in r:
			if c == '-':
				ok = False

		if ok:
			return count

		k = 1
		i = k
		for c in r:
			if c == '-':
				i = k
			k += 1
		
		r = r[0:i]
		rr = ''
		for c in r:
			if c == '-':
				rr = rr + '+'
			else:
				rr = rr + '-'
		r = rr
		count += 1


	return 0


if __name__ == "__main__":
	N = raw_input().strip().split()
	N = int(N[0])
	for i in range(0, N):
		n = flip_pc(raw_input())
		print "Case #" + str(i + 1) + ":", n
		sys.stdout.flush()
