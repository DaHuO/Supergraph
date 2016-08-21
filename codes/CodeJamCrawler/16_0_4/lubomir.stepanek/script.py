###############################################################################
###############################################################################
###############################################################################

## data loading

file_name = "D-small-attempt2.in"

file_pointer = open(file_name, "r")
my_strings = file_pointer.read()
file_pointer.close()


###############################################################################

## preprocessing

data = []

for i in range(1, len(my_strings.split("\n"))):
	if my_strings.split("\n")[i] != "":
		data.append(my_strings.split("\n")[i].split(" "))


###############################################################################

## helper functions

def solveTheCase(K, C, S):
	if K == S:
		return range(1, 1 + K ** C, K ** (C - 1))
	else:
		return "IMPOSSIBLE"


###############################################################################

## core computations

my_indices = []
T = int(my_strings.split("\n")[0])

for i in range(T):
	K, C, S = int(data[i][0]), int(data[i][1]), int(data[i][2])
	my_indices.append(solveTheCase(K,C,S))


###############################################################################

## outputting

output = ""

for i in range(T):
	row = ""
	
	for j in range(len(my_indices[i])):
		row += str(my_indices[i][j]) + " "
	
	output += "Case #" + str(i + 1) + ": " + row + "\n"


###############################################################################

file_name = "D-small-attempt-out.in"

file_pointer = open(file_name, "w")
file_pointer.write(output)
file_pointer.close()


###############################################################################
###############################################################################
###############################################################################






