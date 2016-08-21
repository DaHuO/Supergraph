

f = file("A-large.in")
o = file("sol.out", "w")
cnt = int(f.readline())

for i in xrange(cnt):
	curr = int(f.readline().rstrip())
	if (curr == 0):
		o.write("Case #" + str(i+1) + ": INSOMNIA\n")
	else:
		seen = []
		s = curr
		while len(seen) < 10:
			tmp = s
			while tmp != 0:
				digit = tmp % 10
				tmp = tmp / 10
				if (digit not in seen):
					seen.append(digit)
			print s
			print sorted(seen)
			s += curr
		print sorted(seen)
		o.write("Case #" + str(i+1) + ": " + str(s-curr) + "\n")
