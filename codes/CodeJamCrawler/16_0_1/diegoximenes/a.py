import sys

t = int(raw_input())
for tc in range(1, t+1):
	n = int(raw_input())	
	
	sys.stdout.write("Case #" + str(tc) + ": ")
	
	if n == 0:
		sys.stdout.write("INSOMNIA\n")
		continue

	mark = set()
	i = 1
	while True:
		x = i*n
		for c in str(x): mark.add(c)
		if len(mark) == 10:
			sys.stdout.write(str(x) + "\n")
			break
		i += 1
