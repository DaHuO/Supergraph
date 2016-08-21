"""5
-
-+
+-
+++
--+-

Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3
"""
output = "Case #"
file_object = open("B-large.txt", "r")
text_file = open("Output2.txt", "w")

line =file_object.readlines()
linenum = 0


N = int(line[linenum])
linenum+=1

def flip(stack, ind):
	for i in  range(ind+1):
		if stack[i] == "+":
			stack[i] = "-"
		else:
			stack[i] = "+"
	return stack


for i in range(N):
	counter = 0
	
	case = line[linenum]
	linenum+=1
	
	stack = []
	for cakes in case:
		stack.append(cakes)
	if "\n" in stack:
		stack.remove("\n")
	while "-" in stack:
		for q in range(len(stack)-1, -1,-1):
			if stack[q] == "-":
				stack = flip(stack,q)
				counter +=1

				
	output += str(i+1) + ": "
	output+= str(counter)
	text_file.write(output+"\n")
	output = "Case #"
text_file.close()
	