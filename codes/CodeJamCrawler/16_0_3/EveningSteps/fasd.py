# coding=utf-8

import sys, math, random

def fact(n):
	f = []
	for i in xrange(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			f.append(i)
			while n % i == 0:
				n /= i
	return f

def rand_jc(n):
	mid = ''
	for i in xrange(n - 2):
		mid += str(random.choice([0, 1]))
	return "1" + mid + "1"

def main():
	n, j = 16, 50

	ans = {}
	while len(ans.keys()) < j:
		jc = rand_jc(n)
		current_ans = []
		for base in xrange(2, 11):
			jc_value = sum([int(a) * base**(len(jc) - 1 - i) for i, a in enumerate(jc)])
			factors = fact(jc_value)

			if factors:
				current_ans.append(str(factors[0]))

		if jc not in ans and len(current_ans) == 9:
			ans[jc] = current_ans
			sys.stderr.write("%d more to go!\n" % (j - len(ans.keys())))

	print("Case #1:")
	for jc in ans.keys():
		print("%s %s" % (jc, " ".join(ans[jc])))

if __name__ == '__main__':
	main()