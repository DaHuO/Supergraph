array = []
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
with open("A-large.in", "r") as ins:
    for line in ins:
        array.append(line.splitlines()[0])
array = array[1:]
#print(array)
for i in range(0, int(len(array)/2)):
	num = array[i * 2]
	numlets = array[i * 2 + 1].split()
	results = [int(g) for g in numlets]
	#print(results)
	order = ''
	total = sum(results)
	while total != 0:
		largestpos = 0
		slargestpos = 0
		largestnum = -5
		slargestnum = -5
		for z in range(0, len(results)):
			if results[z] > largestnum:
				slargestnum = largestnum
				largestnum = results[z]
				slargestpos = largestpos
				largestpos = z
			elif results[z] > slargestnum:
				slargestpos = z
				slargestnum = results[z]
		#print(largestpos, slargestpos)
		results[largestpos] -= 1
		total -= 1
		order += " " + letters[largestpos]
		if (total - 1 != 1):
			results[slargestpos] -= 1
			total -= 1
			#print(slargestpos)
			order += letters[slargestpos]
	print("Case #" + str(i + 1) + ":" + order)


