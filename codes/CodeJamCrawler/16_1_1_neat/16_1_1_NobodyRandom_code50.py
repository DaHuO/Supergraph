import sys
def sortIt(N):
	sorted = []
	first = True
	for chara in N:
		val = ord(chara)
		if first:
			sorted.append(val)
			first = False
			continue

		if val < sorted[-1]:
			sorted.append(val)
		elif val >= sorted[0]:
			sorted = [val] + sorted
		else:
			sorted.append(val)
	
	charL = []
	for x in sorted:
		charL.append(chr(x))
	return ''.join(charL)

results = []
firstLine = True
with open("A-large.in") as f:
	contents = f.readlines()
	for content in contents:
		if not firstLine:
			results.append(sortIt(list(content.strip("\n"))))
		firstLine = False;

file = open("a.out", "w")
counter = 1
for item in results:
	file.write("Case #" + str(counter) + ": " + item + "\n")
	counter += 1

file.close()