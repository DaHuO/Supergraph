f = open("B-large.in", "r")
fo = open("output1.txt","w")

count = int(f.readline())

for case in xrange(0,count):
	print case
	pancakes = str(f.readline())
	pancakes = pancakes[::-1].strip()
	count = 0
	lastchar = ''
	beginning = True
	for p in pancakes:
		if beginning:
			if p == '+':
				continue
			else:
				beginning = False
				count += 1
				lastchar = p
		else:
			if p != lastchar:
				count += 1
				lastchar = p
			else:
				continue
	fo.write("Case #" + str(case + 1) + ": " + str(count) + "\n")
