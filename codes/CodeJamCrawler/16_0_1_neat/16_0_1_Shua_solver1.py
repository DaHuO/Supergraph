import sys

file = list(open('A-large.in'))
for i in range(len(file)):
	file[i] = file[i].strip("\n").strip()
#T = file.pop(0)

#parsing will spit out a list


for i in range(1, len(file)):
	sys.stdout.write("Case #" + str(i) + ": ")
	
	if file[i] != "0":
		counter = [];
		# fill counter with -1
		for j in range(10):
			counter.append(-1)
		#print counter
		#print file[i]
		
		n = 0
		
		while -1 in counter:
			n += int(file[i])
			nstr = str(n)
			for c in nstr:
				counter[int(c)] = 0
	
		print n
	else:
		print "INSOMNIA"
