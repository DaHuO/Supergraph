from operator import itemgetter


def max_idx(a):
	return max(enumerate(a), key=itemgetter(1))[0]


def print_evacuation(s):
	plan = []
	n = sum(s)

	while n > 0:
		curr_evac = ""
		ratio = 0.0
		while len(curr_evac) < 2:
			idxp = max_idx(s)
			curr_evac += chr(65 + idxp)
			n -= 1
			s[idxp] -= 1

			if n == 0:
				break

			# if no one is above 0.5, then we can break
			ratio = float(max(s)) / n
			if ratio <= 0.5:
				break
			elif len(curr_evac) == 2:
					# revert the current one
					n += 1
					s[idxp] += 1
					curr_evac = curr_evac[:-1]
					break

		if ratio > 0.5 and n > 0:
			raise Exception("AAAA - %s %f" % (repr(s), ratio))
		plan.append(curr_evac)

	return " ".join(plan)


if __name__ == '__main__':
	import sys
	import time

	start_time = time.time()

	data = file(sys.argv[1], "rb").read()
	lines = data.split('\n')
	out = file(sys.argv[1] + "-sol.dat", "wb")

	for i in xrange(int(lines[0])):
		pnum = int(lines[2*i+1])
		senators = [int(x) for x in lines[2*i+2].strip().split(" ")]

		if pnum != len(senators) or pnum > 26:
			raise Exception("invalid input line %d" % 2*i + 1)

		out.write("Case #%d: %s\n" % (i + 1, print_evacuation(senators)))

	out.close()
	print "--- %s seconds ---" % (time.time() - start_time)
