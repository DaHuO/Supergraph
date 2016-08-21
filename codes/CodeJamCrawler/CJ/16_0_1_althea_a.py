from sys import stdin

cases = int(stdin.readline())
digits = set()
digits = set('0123456789')
for i in range(0, cases):
	N = stdin.readline()
	curr = int(N)
	if (curr != 0):
		seen = set(N)
		while (len(digits - seen) != 0):
			curr += int(N)
			seen.update(set(str(curr)))
		print 'Case #' + str(i+1) + ': ' + str(curr)
	else:
		print 'Case #' + str(i+1) + ': ' + 'INSOMNIA'