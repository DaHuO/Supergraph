#!/usr/bin/python

if __name__ == '__main__':
	t = int(raw_input())
	for i in xrange(t):
		n = int(raw_input())
		all_digits = set()
		if n == 0:
			print 'Case #'+str(i+1)+': INSOMNIA'
		else:
			k = 1
			while True:
				cur_max = str(n*k)
				digits = list(cur_max)
				all_digits = all_digits.union(set(digits))
				if (len(all_digits) == 10):
					print 'Case #'+str(i+1)+': '+cur_max
					break
				k += 1
