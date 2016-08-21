file = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\A-large.in", "r")
output = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\output.txt", "w")

num_cases = int(file.readline())

for i in range(num_cases):
	output.write("Case #" + repr(i + 1) + ": ")
	word = file.readline().strip()
	
	outfilestr = word[0]
	for item in word[1:]:
		if item < outfilestr[0]:
			outfilestr = outfilestr + item
		else:
			outfilestr = item + outfilestr
	

	output.write(outfilestr + "\n")
output.close()
file.close()