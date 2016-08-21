import sys

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = int(raw_input())
	if n > 0:
		found = False
		s = set()
		k = n
		while not found:
			m = k
			while m > 0 and not found:
				s.add(m % 10)
				if len(s) == 10:
					print("CASE #" + str(i) +": " + str(k))
					found = True
				m //= 10
			k += n
	else:
		print("CASE #" + str(i) +": INSOMNIA")
