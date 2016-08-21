import itertools

fd = open("in1", "r")

lines = fd.readlines()

testcases = int(lines[0])

fout = open("out1", "w")

letters = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
exact_letter = ['Z', '', 'W', '', 'U', '', 'X', '', 'G', '']

for line_ind in xrange(1,len(lines)):
	line  = lines[line_ind]
	fout.write("Case #" + str(line_ind) + ": ")

	line_list = list(line.split("\n")[0])

	#print line_list

	final_number = []
	occurences = []
	for i in xrange(0,len(exact_letter)):
		if (not exact_letter[i] == ''):
			occurences.append(line_list.count(exact_letter[i]))
		else:
			occurences.append(0)

	for i in xrange(0,len(exact_letter)):
		occ = occurences[i]
		for j in xrange(0,occ):
			for let in letters[i]:
				line_list.remove(let)
			final_number.append(str(i))


	# Your code here
	
	for num in xrange(0,10):
		flag = True
		while(flag):
			removed = []
			for letter in letters[num]:
				if (letter in line_list):
					line_list.remove(letter)
					removed.append(letter)
				else:
					flag = False
					for removed_l in removed:
						line_list.append(removed_l)
					break
				
			if(flag):
				final_number.append(str(num))

	fout.write("".join(sorted(final_number)) + "\n")
